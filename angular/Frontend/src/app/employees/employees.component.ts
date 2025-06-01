import { Component } from '@angular/core';
import { CommonModule } from '@angular/common'

@Component({
	selector: 'app-employees',
	imports: [CommonModule],
	templateUrl: './employees.component.html',
	styleUrls: ['./employees.component.css']
})
export class EmployeesComponent {
	employees = [
		{
			id : 1 , name : "Anvesh" , salary : 30000  
		},
		{
			id : 2 , name : "Anvesh" , salary : 30000  
		},
		{
			id : 3 , name : "Anvesh" , salary : 30000  
		},
		{
			id : 4 , name : "Anvesh" , salary : 30000  
		}
	]
}
