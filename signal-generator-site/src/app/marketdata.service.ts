import { Injectable } from '@angular/core';
import { Configuration } from './app.constants';
import { Observable, of } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class MarketdataService {

    private marketdataServiceUrl: string;

    constructor(private http: HttpClient, private configuration: Configuration) { 
        this.marketdataServiceUrl = configuration.marketdataUrl;
    }

    public getPropertiesBySymbol(symbol: string): Observable<string[]> {
        return this.http.get<string[]>(this.marketdataServiceUrl + '/' + symbol + '/properties');
    }
}
