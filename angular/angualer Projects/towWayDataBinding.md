# two way data bining 
angular supports two way databining 
- it is the process or methodology to bind the application data from component to view and view to component
- [(ng model)] -> which can be return inside the I/P tag
- inside the app.module.ts:
    - import { formmodules } from '@angular/forms';
- ng new applicationName

```js
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
	selector: 'app-root',
	imports: [ FormsModule],
	templateUrl: './app.component.html',
	styleUrls: ['./app.component.css'],
})

export class AppComponent {
	title = 'mysite';	
	username: string = "Anvesh";
	password: string = "12345678";
}

```

```html
<hr>

<h1>Two way data binding</h1>

<table border="1">
    <tr>
      <td>username: </td>
      <td>
        <input type="text" placeholder="Username " [(ngModel)]="username">
      </td>
    </tr>
    <tr>
      <td>password: </td>
      <td>
        <input type="password" placeholder="password " [(ngModel)]="password">
      </td>
    </tr>
</table>

<hr>

<hr>
<table border="1">
    <tr>
      <th>username</th>
      <th>password</th>
    </tr>
    <tr>
      <td>{{ username }}</td>
      <td>{{ password }}</td>
    </tr>
</table>
```

---
# to create a custom component
- ng generate component Component_name 
- ng g c component_name 
 
---
## questions
1. develop an angualr js and angular application for one way databinding 
2. develop an angular application for one way databinding
3. develop custom components using custom operation 
