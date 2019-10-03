import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ConditionByUserComponent } from './condition-by-user.component';

describe('ConditionByUserComponent', () => {
  let component: ConditionByUserComponent;
  let fixture: ComponentFixture<ConditionByUserComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ConditionByUserComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ConditionByUserComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
