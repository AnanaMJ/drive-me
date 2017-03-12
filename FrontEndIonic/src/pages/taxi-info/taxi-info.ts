import { Component } from '@angular/core';
import { NavController, NavParams } from 'ionic-angular';
import { ServerRequest } from '../service/server-request';
import { HomePage } from '../taxi-request/taxi-request';

@Component({
  selector: 'page-taxi-info',
  templateUrl: 'taxi-info.html',
})
export class TaxiInfoPage {

    companies: Array<any>;
    fromValue: string;
    toValue: string;

    constructor(public navCtrl: NavController, private navParams: NavParams) {
      console.log(navParams);
      console.log(navParams.get('data'));
      this.companies = navParams.get('data');
      console.log(this.fromValue);
      console.log(this.toValue);
      console.log(this.companies);
    }

}
