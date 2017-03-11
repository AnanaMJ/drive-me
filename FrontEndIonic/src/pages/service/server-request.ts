import {Http} from '@angular/http';
import 'rxjs/add/operator/map';

export class ServerRequest {
  static get parameters() {
        return [[Http]];
    }

    constructor(private http:Http) {

    }

    searchTaxi(startLatitude, startLongitude, endLatitude, endLongitude) {
        var url = 'http://google.com';
        var response = this.http.get(url).map(res => res.json());
        return response;
    }
}
