import { Component, ViewChild, ElementRef } from '@angular/core';
import { NavController, LoadingController } from 'ionic-angular';
import { ServerRequest } from '../service/server-request';
import {googlemaps} from 'googlemaps';
import { Geolocation } from 'ionic-native';
import { TaxiInfoPage } from '../taxi-info/taxi-info';


@Component({
  selector: 'page-taxi-request',
  templateUrl: 'taxi-request.html',
  providers: [ServerRequest],
})
export class HomePage {
  fromValue:string;
  toValue:string;
  startLong:number;
  startLat:number;
  endLong:number;
  endLat:number;
  companies:{};
  shouldHeight = document.body.clientHeight + 'px' ;

  constructor(public navCtrl: NavController, public loadingCtrl: LoadingController, private serverRequest: ServerRequest,) {
    this.fromValue = "Current Location";
    this.toValue = "";
    Geolocation.getCurrentPosition().then(pos => {
      this.startLat=pos.coords.latitude;
      this.startLong=pos.coords.longitude;
    });
    this.endLong=0;
    this.endLat=0;
  }


  presentLoadingDefault() {
  let loading = this.loadingCtrl.create({
    content: 'Please wait...',
    dismissOnPageChange: true,
  });

  loading.present();

  setTimeout(() => {
    loading.dismiss();
  }, 50000);
  }

  ngOnInit(){

    // get the two fields
    let input_from = (<HTMLInputElement>document.getElementById("journey_from"));
    let input_to = (<HTMLInputElement>document.getElementById("journey_to"));

    // set the options
    let options = {
    types: [],
    componentRestrictions: {country: "uk"}
    };

    // create the two autocompletes on the from and to fields
    let autocomplete1 = new google.maps.places.Autocomplete(input_from, options);
    let autocomplete2 = new google.maps.places.Autocomplete(input_to, options);

    // we need to save a reference to this as we lose it in the callbacks
    let self = this;

    // add the first listener
    google.maps.event.addListener(autocomplete1, 'place_changed', function() {

    let place = autocomplete1.getPlace();
    self.fromValue = place.name;
    let geometry = place.geometry;
    if ((geometry) !== undefined) {
    console.log(place.name);


    console.log(geometry.location.lng());
    self.startLong = geometry.location.lng();

    console.log(geometry.location.lat());
    self.startLat = geometry.location.lat();

    }});

// add the second listener
    google.maps.event.addListener(autocomplete2, 'place_changed', function() {
    let place = autocomplete2.getPlace();
    self.toValue = place.name;
    let geometry = place.geometry;

    if ((geometry) !== undefined) {

    console.log(place.name);


    console.log(geometry.location.lng());
    self.endLong = geometry.location.lng();

    console.log(geometry.location.lat());
    self.endLat = geometry.location.lat();

    }});

  }

  makeReq() {

    console.log(this.startLat);
    console.log(this.startLong);
    console.log(this.endLat);
    console.log(this.endLong);
    this.presentLoadingDefault();
    this.serverRequest.searchTaxi(this.startLat,this.startLong,this.endLat,this.endLong).subscribe(
      data => {
        this.companies = data;
        console.log(data);
        console.log(data[0][0]);
        console.log(data[0][1].high_price);
        console.log(data.length);
        data.fromValue = this.fromValue;
        data.toValue = this.toValue;
        this.navCtrl.push(TaxiInfoPage, {
          data,
        });

                },
                err => {
                    console.log(err);
                },
                () => console.log('Movie Search Complete')
            );
        }
}
