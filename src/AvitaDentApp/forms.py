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
        ###### ВАРИАНТ № 1 ######
        # widgets = {
            # 'Feedback_name': forms.TextInput(attrs={'autocomplete': 'off', 'type': 'text', 'data-error': 'Ошибка', 'data-value': 'Введите имя', 'class': 'input', 'required': True}),
            # 'Feedback_phone': forms.TextInput(attrs={'autocomplete': 'off', 'type': 'tel', 'data-error': 'Ошибка', 'data-value': 'Введите телефон', 'class': 'input _req _phone', 'required': True}),
        # }
        #########################
        ###### ВАРИАНТ № 2 ######
        # Feedback_name = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off', 'type': 'text', 'data-error': 'Ошибка', 'data-value': 'Введите имя', 'class': 'input', 'required': True}))
        # Feedback_phone = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off', 'type': 'tel', 'data-error': 'Ошибка', 'data-value': 'Введите телефон', 'class': 'input _req _phone', 'required': True}))
        #########################
        ###### ВАРИАНТ № 3 ######
        # widgets = {
            # 'Feedback_name': forms.TextInput(attrs={'autocomplete': 'off', 'type': 'text', 'data-error': 'Ошибка', 'data-value': 'Введите имя', 'class': 'form-input', 'required': True}),
            # 'Feedback_phone': forms.TextInput(attrs={'autocomplete': 'off', 'type': 'tel', 'data-error': 'Ошибка', 'data-value': 'Введите телефон', 'class': 'form-input', 'required': True}),
        # }
        #########################
        
        
#<div class="popup__form">
#    <form action="mail.php" method="post">
#        <h2>Оставьте заявку на консультацию</h2>
#        <p>Наши менеджеры свяжутся с вами в течение 10 минут</p>
#        <input autocomplete="off" name="name" type="text" name="form[]" data-error="Ошибка" data-value="Введите имя" class="input" />
#        <input autocomplete="off" name="phone" type="tel" name="form[]" data-error="Ошибка" data-value="Телефон" class="input _req _phone" />
#        <button type="submit" class="btn-sub main-link">Отправить заявку</button>
#        <p>Нажимая на кнопку вы соглашаетесь на обработку <a href="{% url 'privacy-policy' %}">персональных данных</a></p>
#    </form>
#</div>