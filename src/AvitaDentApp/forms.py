from django import forms

#from KinomonsterApp.models import Film, Series, FilmComments, SeriesComments, SendMessage
from .models import Feedback

#from django.contrib.auth import get_user_model, authenticate
#from django.contrib.auth.hashers import check_password

#from django.contrib.auth.models import User

#from django.contrib.auth.forms import UserCreationForm

from django.core.mail import send_mail



class FeedbackForm(forms.ModelForm):
    
    class Meta:
        model = Feedback
        fields = ['Feedback_name', 'Feedback_phone']
        widgets = {
            'Feedback_name': forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'Заголовок текста'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': '9', 'placeholder': 'Текст'}),
        }
        
        
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