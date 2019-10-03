import { Component, OnInit, Input } from '@angular/core';
import { Condition } from '../condition';
import { ConditionService } from "../condition.service';

@Component({
  selector: 'app-condition-by-user',
  templateUrl: './condition-by-user.component.html',
  styleUrls: ['./condition-by-user.component.css']
})
export class ConditionByUserComponent implements OnInit {
    @Input userId: number; 
    conditionsForUser: Condition[];

    constructor(private conditionService: ConditionService) { }

    ngOnInit() {
    }

}
