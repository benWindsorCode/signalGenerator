import { Injectable } from '@angular/core';

@Injectable({
    providedIn:'root'
})
export class Configuration {
    public base = 'http://127.0.0.1'
    public marketdataEndpoint = ':5010/marketdata'
    public marketdataUrl = this.base + this.marketdataEndpoint
    public conditionEndpoint = ':6001/condition'
    public conditionUrl = this.base + this.conditionEndpoint
}
