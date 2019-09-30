import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ConditionCreatorComponent } from './condition-creator.component';

describe('ConditionCreatorComponent', () => {
  let component: ConditionCreatorComponent;
  let fixture: ComponentFixture<ConditionCreatorComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ConditionCreatorComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ConditionCreatorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
