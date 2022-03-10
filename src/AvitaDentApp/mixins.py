from django.views.generic import View
from .models import *
from .forms import FeedbackForm
#from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from django.contrib import auth
from django.http import HttpResponseRedirect


class MyFormMixin(View):

    def dispatch(self, request, *args, **kwargs):
        #################### РЕАЛИЗУЕМ ПОЛУЧЕНИЕ ЗАЯВКИ ОТ ПОЛЬЗОВАТЕЛЯ: ####################
        if request.method == 'POST' and 'feedback' in request.POST:
            feedback_form = FeedbackForm(request.POST)
            if feedback_form.is_valid():
                feedback_form.save()
                Feedback_name = feedback_form.cleaned_data.get('Feedback_name')
                print(Feedback_name)
                Feedback_phone = feedback_form.cleaned_data.get('Feedback_phone')
                print(Feedback_phone)
                print("ВАША ЗАЯВКА УСПЕШНО ОТПРАВЛЕНА!")
                return HttpResponseRedirect(self.request.path)
            else:
                print("ЧТО-ТО ПОШЛО НЕ ТАК!")
                messages.error(request, 'ВАША ЗАЯВКА НЕ ОТПРАВЛЕНА!')
                return HttpResponseRedirect(self.request.path)
        else:
            self.feedback_form = FeedbackForm()
        #####################################################################################
        # print(F'request.path == {request.path}')
        return super().dispatch(request, *args, **kwargs)