from rest_framework import serializers
from passApp.models import Passenger


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id', 'firstName', 'lastName', 'travelPoints']
