import { Component, OnInit } from '@angular/core';
import { Condition } from '../condition';
import { HttpHeaders } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-condition-creator',
  templateUrl: './condition-creator.component.html',
  styleUrls: ['./condition-creator.component.css']
})
export class ConditionCreatorComponent implements OnInit {
    notification_methods = ['SMS', 'email', 'SMS+email']

    httpOptions = {
        headers: new HttpHeaders({
            'Content-Type':  'application/json'
        })
    };

    model = new Condition();
    submitted = false;
    conditionUrl = "http://127.0.0.1:6001/condition/add";

    constructor(private http: HttpClient) { }

    ngOnInit() {
    }

    onSubmit() {
        this.submitted = true;
        console.log(this.submitted);
    }

    newCondition() {
        console.log(this.model);
        return this.http.post<Condition>(this.conditionUrl, this.model, this.httpOptions)
            .subscribe(
                (val) => console.log(val),
                error => console.log(error),
                () => console.log("Complete")
                )
    }

    handleError() {
        console.log("Error in submission")
    }

}
