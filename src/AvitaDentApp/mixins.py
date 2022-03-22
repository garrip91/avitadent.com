from django.views.generic import View
from .models import *
from .forms import FeedbackForm, AppointmentForm
#from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from django.contrib import auth
from django.http import HttpResponseRedirect


class MyFormMixin1(View):

    def dispatch(self, request, *args, **kwargs):
        #################### РЕАЛИЗУЕМ ПОЛУЧЕНИЕ ЗАЯВКИ ОТ ПОЛЬЗОВАТЕЛЯ: ####################
        if request.method == 'POST' and 'feedback1' in request.POST:
            feedback_form = FeedbackForm(request.POST)
            print(feedback_form)
            if feedback_form.is_valid():
                feedback_form.save()
                Feedback_name = feedback_form.cleaned_data.get('Feedback_name')
                print(Feedback_name)
                Feedback_phone = feedback_form.cleaned_data.get('Feedback_phone')
                print(Feedback_phone)
                print("ВАША ЗАЯВКА УСПЕШНО ОТПРАВЛЕНА!")
                messages.success(request, "ВАША ЗАЯВКА УСПЕШНО ОТПРАВЛЕНА!")
                #return HttpResponseRedirect(self.request.path)
                return HttpResponseRedirect(F'{self.request.path}#thanks')
            else:
                print("ЧТО-ТО ПОШЛО НЕ ТАК!")
                messages.error(request, 'НЕПРАВИЛЬНО ВВЕДЁН НОМЕР ТЕЛЕФОНА!')
                #return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
                return HttpResponseRedirect(self.request.path)
        else:
            self.feedback_form = FeedbackForm()
        #####################################################################################
        # print(F'request.path == {request.path}')
        return super().dispatch(request, *args, **kwargs)


class MyFormMixin2(View):

    def dispatch(self, request, *args, **kwargs):
        #################### РЕАЛИЗУЕМ ПОЛУЧЕНИЕ ЗАЯВКИ ОТ ПОЛЬЗОВАТЕЛЯ: ####################
        if request.method == 'POST' and 'feedback2' in request.POST:
            appointment_form = AppointmentForm(request.POST)
            print(appointment_form)
            if appointment_form.is_valid():
                appointment_form.save()
                Appointment_name = appointment_form.cleaned_data.get('Appointment_name')
                print(Appointment_name)
                Appointment_phone = appointment_form.cleaned_data.get('Appointment_phone')
                print(Appointment_phone)
                Appointment_email = appointment_form.cleaned_data.get('Appointment_email')
                print(Appointment_email)
                print("ВАША ЗАЯВКА УСПЕШНО ОТПРАВЛЕНА!")
                messages.success(request, "ВАША ЗАЯВКА УСПЕШНО ОТПРАВЛЕНА!")
                #return HttpResponseRedirect(self.request.path)
                return HttpResponseRedirect(F'{self.request.path}#thanks')
            else:
                print("ЧТО-ТО ПОШЛО НЕ ТАК!")
                messages.error(request, 'НЕПРАВИЛЬНО ВВЕДЁН НОМЕР ТЕЛЕФОНА!')
                #return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
                return HttpResponseRedirect(self.request.path)
        else:
            self.appointment_form = AppointmentForm()
        #####################################################################################
        # print(F'request.path == {request.path}')
        return super().dispatch(request, *args, **kwargs)