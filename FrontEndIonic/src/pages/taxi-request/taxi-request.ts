import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import {ServerRequest} from '../service/server-request';

@Component({
  selector: 'page-taxi-request',
  templateUrl: 'taxi-request.html',
  providers: [ServerRequest]
})
export class HomePage {

  constructor(public navCtrl: NavController) {

  }

}
