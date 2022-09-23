from dataclasses import fields
from datetime import datetime
from pyexpat import model
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.core.mail import send_mail

from .models import *

class RadioSerializer(serializers.ModelSerializer):

    class Meta:
        model = RadioStationModel
        fields = '__all__'

class FavouritesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavouritesModel
        fields = '__all__'