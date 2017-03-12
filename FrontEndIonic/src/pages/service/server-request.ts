import {Http} from '@angular/http';
import 'rxjs/add/operator/map';

export class ServerRequest {
  static get parameters() {
        return [[Http]];
    }

    constructor(private http:Http) {

    }

    searchTaxi(startLatitude, startLongitude, endLatitude, endLongitude) {
        var url = 'http://c34d0c13.ngrok.io/estimate/startLat=';
        url += encodeURI(startLatitude) + "&startLon=" + encodeURI(startLongitude) + "&endLat=" + encodeURI(endLatitude) + "&endLon=" + encodeURI(endLongitude);
        var response = this.http.get(url).map(res => res.json());
        return response;
    }
}
