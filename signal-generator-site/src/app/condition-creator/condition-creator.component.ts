import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-condition-creator',
  templateUrl: './condition-creator.component.html',
  styleUrls: ['./condition-creator.component.css']
})
export class ConditionCreatorComponent implements OnInit {
    notification_methods = ['SMS', 'email', 'SMS+email']

  constructor() { }

  ngOnInit() {
  }

}
