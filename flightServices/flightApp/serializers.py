from rest_framework import serializers
from flightApp.models import Flight, Passenger, Reservation
import re


def isValidFlightNumber(flightnumber):
    regex = re.compile('^[A-Z]{2}[0-9]{2}$')
    return regex.match(flightnumber)


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        validators = [isValidFlightNumber]

    def validate_flightNumber(self, value):
        if re.match(r'^[a-zA-Z0-9]*$', value) is None:
            raise serializers.ValidationError("Flight number does not match")
        return value

    def validate(self, data):
        print(data)
        return data


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
