import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Criteria } from 'src/app/model/criteria';
import { LoginService } from 'src/app/services/login.service';
import { ReservationService } from 'src/app/services/reservation.service';

@Component({
  selector: 'app-find-flights',
  templateUrl: './find-flights.component.html',
  styleUrls: ['./find-flights.component.scss']
})
export class FindFlightsComponent implements OnInit {
  criteria: Criteria = new Criteria('','','');

  constructor(
    private loginService: LoginService,
    private reservationService: ReservationService,
    private router: Router
    ) { }

  ngOnInit(): void {
    this.loginService.login();
  }

  onSubmit() {
    this.reservationService.getFlights(this.criteria).subscribe(res => {
      this.reservationService.flightData = res;
      this.router.navigate(['/displayFlights']);
    });
  }

}
