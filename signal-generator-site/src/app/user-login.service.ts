import { Injectable } from '@angular/core';
import { CognitoCallback, CognitoService, LoggedInCallback } from "./cognito.service";
import { AuthenticationDetails, CognitoUser, CognitoUserSession } from "amazon-cognito-identity-js";
import * as AWS from "aws-sdk/global";
import * as STS from "aws-sdk/clients/sts";

@Injectable({
  providedIn: 'root'
})
export class UserLoginService {

  private sts_endpoint = '';

  private onLoginSuccess = (callback: CognitoCallback, session: CognitoUserSession) => {

    console.log("In authenticateUser onSuccess callback");

    AWS.config.credentials = this.cognitoService.buildCognitoCreds(session.getIdToken().getJwtToken());

    let clientParams: any = {};
    if (this.sts_endpoint) {
        clientParams.endpoint = this.sts_endpoint;
    }
    let sts = new STS(clientParams);
    sts.getCallerIdentity(function (err, data) {
        console.log("UserLoginService: Successfully set the AWS credentials");
        callback.cognitoCallback(null, session);
    });
}

private onLoginError = (callback: CognitoCallback, err) => {
    callback.cognitoCallback(err.message, null);
}

constructor(public cognitoService: CognitoService) {
}

authenticate(username: string, password: string, callback: CognitoCallback) {
    console.log("UserLoginService: starting the authentication");

    let authenticationData = {
        Username: username,
        Password: password,
    };
    let authenticationDetails = new AuthenticationDetails(authenticationData);

    let userData = {
        Username: username,
        Pool: this.cognitoService.getUserPool()
    };

    console.log("UserLoginService: Params set...Authenticating the user");
    let cognitoUser = new CognitoUser(userData);
    console.log("UserLoginService: config is " + AWS.config);
    cognitoUser.authenticateUser(authenticationDetails, {
        newPasswordRequired: (userAttributes, requiredAttributes) => callback.cognitoCallback(`User needs to set password.`, null),
        onSuccess: result => this.onLoginSuccess(callback, result),
        onFailure: err => this.onLoginError(callback, err),
        mfaRequired: (challengeName, challengeParameters) => {
            callback.handleMFAStep(challengeName, challengeParameters, (confirmationCode: string) => {
                cognitoUser.sendMFACode(confirmationCode, {
                    onSuccess: result => this.onLoginSuccess(callback, result),
                    onFailure: err => this.onLoginError(callback, err)
                });
            });
        }
    });
}

forgotPassword(username: string, callback: CognitoCallback) {
    let userData = {
        Username: username,
        Pool: this.cognitoService.getUserPool()
    };

    let cognitoUser = new CognitoUser(userData);

    cognitoUser.forgotPassword({
        onSuccess: function () {

        },
        onFailure: function (err) {
            callback.cognitoCallback(err.message, null);
        },
        inputVerificationCode() {
            callback.cognitoCallback(null, null);
        }
    });
}

confirmNewPassword(email: string, verificationCode: string, password: string, callback: CognitoCallback) {
    let userData = {
        Username: email,
        Pool: this.cognitoService.getUserPool()
    };

    let cognitoUser = new CognitoUser(userData);

    cognitoUser.confirmPassword(verificationCode, password, {
        onSuccess: function () {
            callback.cognitoCallback(null, null);
        },
        onFailure: function (err) {
            callback.cognitoCallback(err.message, null);
        }
    });
}

logout() {
    console.log("User Logging out");
    this.cognitoService.getCurrentUser().signOut();

}

isAuthenticated(callback: LoggedInCallback) {
    if (callback == null)
        throw("UserLoginService: Callback in isAuthenticated() cannot be null");

    let cognitoUser = this.cognitoService.getCurrentUser();

    if (cognitoUser != null) {
        cognitoUser.getSession(function (err, session) {
            if (err) {
                console.log("UserLoginService: Couldn't get the session: " + err, err.stack);
                callback.isLoggedIn(err, false);
            }
            else {
                console.log("UserLoginService: Session is " + session.isValid());
                callback.isLoggedIn(err, session.isValid());
            }
        });
    } else {
        console.log("UserLoginService: can't retrieve the current user");
        callback.isLoggedIn("Can't retrieve the CurrentUser", false);
    }
}
}