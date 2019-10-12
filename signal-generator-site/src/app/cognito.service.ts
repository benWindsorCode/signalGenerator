import { Injectable } from '@angular/core';
import { CognitoUserPool } from "amazon-cognito-identity-js";
import * as AWS from "aws-sdk/global";
import * as awsservice from "aws-sdk/lib/service";
import * as CognitoIdentity from "aws-sdk/clients/cognitoidentity";
import { Secrets } from './app.secrets';

@Injectable({
  providedIn: 'root'
})
export class CognitoService {

  constructor(private secrets: Secrets) { }
  public  _REGION = "eu-west-1"

    public  _IDENTITY_POOL_ID = this.secrets.identityId;
    public  _USER_POOL_ID = this.secrets.userPoolId;
    public  _CLIENT_ID = this.secrets.clientId;
    public cognito_idp_endpoint = '';
    public cognito_identity_endpoint = '';

    public _POOL_DATA: any = {
        UserPoolId: this._USER_POOL_ID,
        ClientId: this._CLIENT_ID
    };

    public cognitoCreds: AWS.CognitoIdentityCredentials;

    getUserPool() {
        if (this.cognito_idp_endpoint) {
            this._POOL_DATA.endpoint = this.cognito_idp_endpoint;
        }
        return new CognitoUserPool(this._POOL_DATA);
    }

    getCurrentUser() {
        return this.getUserPool().getCurrentUser();
    }

    setCognitoCreds(creds: AWS.CognitoIdentityCredentials) {
        this.cognitoCreds = creds;
    }

    getCognitoCreds() {
        return this.cognitoCreds;
    }

    buildCognitoCreds(idTokenJwt: string) {
        let url = 'cognito-idp.' + this._REGION.toLowerCase() + '.amazonaws.com/' + this._USER_POOL_ID;
        if (this.cognito_idp_endpoint) {
            url = this.cognito_idp_endpoint + '/' + this._USER_POOL_ID;
        }
        let logins: CognitoIdentity.LoginsMap = {};
        logins[url] = idTokenJwt;
        let params = {
            IdentityPoolId: this._IDENTITY_POOL_ID, /* required */
            Logins: logins
        };
        let serviceConfigs = <awsservice.ServiceConfigurationOptions>{};
        if (this.cognito_identity_endpoint) {
            serviceConfigs.endpoint = this.cognito_identity_endpoint;
        }
        let creds = new AWS.CognitoIdentityCredentials(params, serviceConfigs);
        this.setCognitoCreds(creds);
        return creds;
    }


    getCognitoIdentity(): string {
        return this.cognitoCreds.identityId;
    }

    getAccessToken(callback: Callback): void {
        if (callback == null) {
            throw("CognitoUtil: callback in getAccessToken is null...returning");
        }
        if (this.getCurrentUser() != null) {
            this.getCurrentUser().getSession(function (err, session) {
                if (err) {
                    console.log("CognitoUtil: Can't set the credentials:" + err);
                    callback.callbackWithParam(null);
                }
                else {
                    if (session.isValid()) {
                        callback.callbackWithParam(session.getAccessToken().getJwtToken());
                    }
                }
            });
        }
        else {
            callback.callbackWithParam(null);
        }
    }

    getIdToken(callback: Callback): void {
        if (callback == null) {
            throw("CognitoUtil: callback in getIdToken is null...returning");
        }
        if (this.getCurrentUser() != null)
            this.getCurrentUser().getSession(function (err, session) {
                if (err) {
                    console.log("CognitoUtil: Can't set the credentials:" + err);
                    callback.callbackWithParam(null);
                }
                else {
                    if (session.isValid()) {
                        callback.callbackWithParam(session.getIdToken().getJwtToken());
                    } else {
                        console.log("CognitoUtil: Got the id token, but the session isn't valid");
                    }
                }
            });
        else
            callback.callbackWithParam(null);
    }

    getRefreshToken(callback: Callback): void {
        if (callback == null) {
            throw("CognitoUtil: callback in getRefreshToken is null...returning");
        }
        if (this.getCurrentUser() != null)
            this.getCurrentUser().getSession(function (err, session) {
                if (err) {
                    console.log("CognitoUtil: Can't set the credentials:" + err);
                    callback.callbackWithParam(null);
                }

                else {
                    if (session.isValid()) {
                        callback.callbackWithParam(session.getRefreshToken());
                    }
                }
            });
        else
            callback.callbackWithParam(null);
    }

    refresh(): void {
        this.getCurrentUser().getSession(function (err, session) {
            if (err) {
                console.log("CognitoUtil: Can't set the credentials:" + err);
            }

            else {
                if (session.isValid()) {
                    console.log("CognitoUtil: refreshed successfully");
                } else {
                    console.log("CognitoUtil: refreshed but session is still not valid");
                }
            }
        });
    }
}

export interface CognitoCallback {
    cognitoCallback(message: string, result: any): void;

    handleMFAStep?(challengeName: string, challengeParameters: ChallengeParameters, callback: (confirmationCode: string) => any): void;
}

export interface LoggedInCallback {
    isLoggedIn(message: string, loggedIn: boolean): void;
}

export interface ChallengeParameters {
    CODE_DELIVERY_DELIVERY_MEDIUM: string;

    CODE_DELIVERY_DESTINATION: string;
}

export interface Callback {
    callback(): void;

    callbackWithParam(result: any): void;
}
