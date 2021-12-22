import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ReservationService } from 'src/app/services/reservation.service';

@Component({
  selector: 'app-display-flights',
  templateUrl: './display-flights.component.html',
  styleUrls: ['./display-flights.component.scss']
})
export class DisplayFlightsComponent implements OnInit {
  data: any;

  constructor(
    private service: ReservationService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.data = this.service.flightData;
  }

  onSelect(flightID: number) {
    console.log(flightID);
    this.router.navigate([`/passengerDetails/${flightID}`]);
  }

}
