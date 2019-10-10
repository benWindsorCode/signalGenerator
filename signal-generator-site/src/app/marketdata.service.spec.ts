import { TestBed } from '@angular/core/testing';

import { MarketdataService } from './marketdata.service';

describe('MarketdataService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: MarketdataService = TestBed.get(MarketdataService);
    expect(service).toBeTruthy();
  });
});
