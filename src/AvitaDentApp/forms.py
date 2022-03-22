from django import forms

#from KinomonsterApp.models import Film, Series, FilmComments, SeriesComments, SendMessage
from .models import Feedback

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