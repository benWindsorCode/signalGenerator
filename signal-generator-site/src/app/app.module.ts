import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { MatTabsModule } from '@angular/material/tabs';
import { MatCardModule } from '@angular/material/card';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatToolbarModule } from '@angular/material/toolbar';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ConditionCreatorComponent } from './condition-creator/condition-creator.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ConditionByUserComponent } from './condition-by-user/condition-by-user.component';
import { ConditionItemComponent } from './condition-item/condition-item.component';
import { TabbedContainerComponent } from './tabbed-container/tabbed-container.component';
import { UserLoginComponent } from './user-login/user-login.component';

@NgModule({
  declarations: [
    AppComponent,
    ConditionCreatorComponent,
    ConditionByUserComponent,
    ConditionItemComponent,
    TabbedContainerComponent,
    UserLoginComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatTabsModule,
    MatCardModule,
    MatSidenavModule,
    MatToolbarModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
