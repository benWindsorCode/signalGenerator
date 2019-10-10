import { Component, OnInit } from '@angular/core';
import { Condition } from '../condition';
import { HttpHeaders } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';
import { ConditionService } from '../condition.service';
import { MarketdataService } from '../marketdata.service';

@Component({
  selector: 'app-condition-creator',
  templateUrl: './condition-creator.component.html',
  styleUrls: ['./condition-creator.component.css']
})
export class ConditionCreatorComponent implements OnInit {
    notification_methods = ['SMS', 'EMAIL', 'BOTH']

    httpOptions = {
        headers: new HttpHeaders({
            'Content-Type':  'application/json'
        })
    };

    model = new Condition();
    submitted = false;
    properties;

    constructor(private http: HttpClient, 
        private conditionService: ConditionService,
        private marketdataService: MarketdataService) { 
        this.properties = ["Click 'See Properties' to load available properties"]
    }

    ngOnInit() {
    }

    onSubmit() {
        this.submitted = true;
        console.log(this.submitted);
    }

    newCondition() {
        console.log(this.model);
        return this.conditionService.addCondition(this.model)
            .subscribe(
                (val) => console.log(val),
                error => console.log(error),
                () => console.log("Complete")
                );
    }

    getProperties() {
        this.marketdataService.getPropertiesBySymbol(this.model.symbol)
            .subscribe(
                (val) => this.properties=val,
                error => this.properties=["Failed to fetch properties for: "+this.model.symbol],
                () => console.log('Marketdata fetched for'+this.model.symbol)
            );

    }

    handleError() {
        console.log("Error in submission")
    }

}
