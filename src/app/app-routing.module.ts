import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TextFormComponent } from './text-form/text-form.component';
import { TextViewComponent } from './text-view/text-view.component';

const routes: Routes = [
  { path: '', component: TextFormComponent },
  { path: 'view/:id', component: TextViewComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }