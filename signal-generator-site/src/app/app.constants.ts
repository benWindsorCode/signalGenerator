import { Injectable } from '@angular/core';

@Injectable()
export class Configuration {
    public base = 'http://127.0.0.1'
    public marketdata_endpoint = ':5010/marketdata'
    public marketdata_url = this.base + this.marketdata_endpoint
    public condition_endpoint = ':6001/condition'
    public condition_url = this.base + this.condition_endpoint
}
