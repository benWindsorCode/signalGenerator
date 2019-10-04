import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { MatTabsModule } from '@angular/material/tabs';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ConditionCreatorComponent } from './condition-creator/condition-creator.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ConditionByUserComponent } from './condition-by-user/condition-by-user.component';
import { ConditionItemComponent } from './condition-item/condition-item.component';

@NgModule({
  declarations: [
    AppComponent,
    ConditionCreatorComponent,
    ConditionByUserComponent,
    ConditionItemComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatTabsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
