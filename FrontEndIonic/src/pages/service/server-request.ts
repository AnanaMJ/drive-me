import {Http} from '@angular/http';
import 'rxjs/add/operator/map';

export class ServerRequest {
  static get parameters() {
        return [[Http]];
    }

    constructor(private http:Http) {

    }

    searchTaxi(startLatitude, startLongitude, endLatitude, endLongitude) {
        var url = 'http://api.themoviedb.org/3/search/movie?query=&query=' + encodeURI(startLatitude) + encodeURI(startLongitude) + encodeURI(endLatitude) + encodeURI(endLongitude);
        var response = this.http.get(url).map(res => res.json());
        return response;
    }
}
