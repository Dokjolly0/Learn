//node-modules
import { bootstrapApplication } from '@angular/platform-browser';
//local modules
import { AppComponent } from './app/app.component';
//import {HeaderComponent} from "./app/header.component";

bootstrapApplication(AppComponent).catch((err) => console.error(err));
//bootstrapApplication(HeaderComponent).catch((err) => console.error(err)); //Non è il metodo giusto
