import { NgModule, ErrorHandler } from '@angular/core';
import { IonicApp, IonicModule, IonicErrorHandler } from 'ionic-angular';
import { MyApp } from './app.component';
import { HomePage } from '../pages/taxi-request/taxi-request';
import { ServerRequest } from '../pages/service/server-request';
import { TaxiInfoPage } from '../pages/taxi-info/taxi-info';

@NgModule({
  declarations: [
    MyApp,
    HomePage,
    TaxiInfoPage
  ],
  imports: [
    IonicModule.forRoot(MyApp)
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    HomePage,
    TaxiInfoPage
  ],
  providers: [{provide: ErrorHandler, useClass: IonicErrorHandler}]
})
export class AppModule {}
