import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { TabbedContainerComponent } from './tabbed-container/tabbed-container.component';
import { UserLoginComponent } from './user-login/user-login.component';


const routes: Routes = [
    { path: '', component: UserLoginComponent },
    { path: 'home', component: TabbedContainerComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
