import { Component } from '@angular/core';
import { ConditionCreatorComponent } from './condition-creator/condition-creator.component';
import { MatTabsModule } from '@angular/material/tabs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Signal Generator';
}
