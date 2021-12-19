from django.shortcuts import render
from flightApp.models import Flight, Passenger, Reservation
from flightApp.serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def find_flights(request):
    flights = Flight.objects.filter(
        departureCity=request.data['departureCity'],
        arrivalCity=request.data['arrivalCity'],
        dateOfDeparture=request.data['dateOfDeparture'],
    )
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def save_reservation(request):
    Reservation.objects.create(
        flight=Flight.objects.get(id=request.data['flightId']),
        passenger=Passenger.objects.create(
            firstName=request.data['firstName'],
            lastName=request.data['lastName'],
            middleName=request.data['middleName'],
            email=request.data['email'],
            phone=request.data['phone'],
        ),
    )
    return Response(status=status.HTTP_201_CREATED)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsAuthenticated,)


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
