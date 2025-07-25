import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { LeftComponent } from './left/left.component';
import { RightComponent } from './right/right.component';

@Component({
	selector: 'app-root',
	imports: [
		HeaderComponent,
		FooterComponent,
		LeftComponent,
		RightComponent
	],
	templateUrl: './app.component.html',
	styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'BasicComponents';
}
