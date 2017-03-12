import { Component } from '@angular/core';
import { NavController, NavParams } from 'ionic-angular';
import { ServerRequest } from '../service/server-request';
import { HomePage } from '../taxi-request/taxi-request';
import { AlertController } from 'ionic-angular';

@Component({
  selector: 'page-taxi-info',
  templateUrl: 'taxi-info.html',
})
export class TaxiInfoPage {

    companies: Array<any>;
    fromValue: string;
    toValue: string;

    constructor(public navCtrl: NavController, private navParams: NavParams, public alertCtrl: AlertController) {
      console.log(navParams);
      console.log(navParams.get('data'));
      this.companies = navParams.get('data');
      console.log(this.fromValue);
      console.log(this.toValue);
      console.log(this.companies);
    }

    showPrompt(){
      let prompt = this.alertCtrl.create({
        title: 'Order Taxi',
        message: 'Enter your username and password',
        inputs: [
        {
          name: 'username',
          type: 'email',
          placeholder: 'Username',
        },
        {
          name: 'password',
          type: 'password',
          placeholder: 'password',
        },
        ],
        buttons: [
          {
            text: 'Cancel',
            handler: data => {
              console.log("CANCEL");
            }
          },
          {
            text: 'Order',
            handler: data => {
              console.log("SAVE");
              this.showAlert();
            }
          }
        ]
      });
      prompt.present();
    }

    showAlert() {
    let alert = this.alertCtrl.create({
      title: 'Taxi has been booked!',
      subTitle: 'Your taxi has been ordered! Stay tuned for more information',
      buttons: [
      {
        text: 'OK',
        handler: data => {
          this.navCtrl.pop();
        }
      }
      ]
    });
    alert.present();
  }

}
