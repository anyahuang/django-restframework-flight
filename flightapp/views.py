from django.shortcuts import render
from flightapp.models import Flight, Passenger, Reservation
from flightapp.serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status 
from rest_framework import permissions

# make a search flight function
@api_view(['POST'])
def find_flights(request):
      flights = Flight.objects.filter(departureCity=request.data['departureCity'], arrivalCity=request.data['arrivalCity'], dateOfDeparture=request.data['dateOfDeparture'])
      serializer=FlightSerializer(flights,many=True)
      return Response(serializer.data)


@api_view(['POST'])
def save_reservation(request):
      flight = Flight.objects.get(id=request.data['flightId'])
      flight.save()
       
      passenger=Passenger()
      passenger.firstName=request.data['firstName']
      passenger.lastName=request.data['lastName'] 
      passenger.email=request.data['email'] 
      passenger.phone=request.data['phone']
     
      passenger.save()
      
      reservation=Reservation()
      reservation.flight=flight
      reservation.passenger=passenger
      
      reservation.save()
      return Response(status=status.HTTP_201_CREATED)
      

class FlightViewSet(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class PassengerViewSet(viewsets.ModelViewSet):
    queryset=Passenger.objects.all()
    serializer_class=PassengerSerializer    
    
class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer    
    permission_classes = [permissions.IsAuthenticated]
