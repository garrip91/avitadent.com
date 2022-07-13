from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Doctors


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class DoctorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctors
        fields = ['Doctors_webp', 'Doctors_image', 'Doctors_name', 'Doctors_about']