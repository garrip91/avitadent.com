from django import forms

#from KinomonsterApp.models import Film, Series, FilmComments, SeriesComments, SendMessage
from .models import Feedback, Appointment

#from django.contrib.auth import get_user_model, authenticate
#from django.contrib.auth.hashers import check_password

#from django.contrib.auth.models import User

#from django.contrib.auth.forms import UserCreationForm

#from django.core.mail import send_mail

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget



class FeedbackForm(forms.ModelForm):
    
    class Meta:
        model = Feedback
        fields = ['Feedback_name', 'Feedback_phone']
        Feedback_name = forms.CharField(required=True)
        Feedback_phone = forms.CharField(required=True)


class AppointmentForm(forms.ModelForm):
    
    class Meta:
        model = Appointment
        fields = ['Appointment_name', 'Appointment_phone', 'Appointment_email']
        Appointment_name = forms.CharField(required=True)
        Appointment_phone = forms.CharField(required=True)
        Appointment_email = forms.EmailField(required=True)


class FooterFeedbackForm(forms.ModelForm):
    
    class Meta:
        model = Feedback
        fields = ['Feedback_name', 'Feedback_phone']
        FooterFeedback_name = forms.CharField(required=True)
        FooterFeedback_phone = forms.CharField(required=True)