import { Injectable } from '@angular/core';
import { Condition } from  './condition';
import { Observable, of } from 'rxjs';
import { Configuration } from './app.constants';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ConditionService {

    private conditionServiceUrl: string;
    private addConditionUrl: string;
    private getConditionByUserUrl: string;

    constructor(private http: HttpClient, private configuration: Configuration) { 
        this.conditionServiceUrl = configuration.conditionUrl;
        this.addConditionUrl = this.conditionServiceUrl + '/add';
        this.getConditionByUserUrl = this.conditionServiceUrl + '/user/'
    }

    public addCondition(newCondition : Condition): Observable<Condition> {
        // do we need http options here?
        return this.http.post<Condition>(this.addConditionUrl, newCondition);
    }

    public getConditionsByUser(user_id: int): Observable<Condition[]> {
        return this.http.get<Condition[]>(this.getConditionByUserUrl + user_id);
    }

}
