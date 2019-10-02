import { Injectable } from '@angular/core';
import { Condition } from  './condition';
import { Observable, of } from 'rxjs';
import { Configuration } from './app.constants';

@Injectable({
  providedIn: 'root'
})
export class ConditionService {

  private add_condition: string;

  constructor(private configuration: Configuration) { }
}
