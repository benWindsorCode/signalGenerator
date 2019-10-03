import { Component, OnInit, Input } from '@angular/core';
import { Condition } from '../condition';

@Component({
  selector: 'app-condition-item',
  templateUrl: './condition-item.component.html',
  styleUrls: ['./condition-item.component.css']
})
export class ConditionItemComponent implements OnInit {
    @Input inputCondition: Condition;

    constructor() { }

    ngOnInit() {
    }

}
