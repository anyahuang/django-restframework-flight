from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver # a decorector
from rest_framework.authtoken.models import Token
from django.conf import settings
# Create your models here.

class Flight(models.Model):
    flightNumber=models.CharField(max_length=10)
    airline = models.CharField(max_length=30)
    departureCity=models.CharField(max_length=30)
    arrivalCity=models.CharField(max_length=30)
    dateOfDeparture=models.DateField()
    estimatedTimeOfDeparture=models.TimeField()
    
class Passenger(models.Model):
    firstName= models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)   
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=30)
    
class Reservation(models.Model):
    flight=models.ForeignKey(Flight,on_delete=models.CASCADE)
    passenger=models.OneToOneField(Passenger,on_delete=models.CASCADE)    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender,instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
