from django.views.generic import View
from .models import *
from .forms import FeedbackForm, AppointmentForm, FooterFeedbackForm
from django.contrib import messages
from django.http import HttpResponseRedirect

from django.core.mail import send_mail
from django.http import HttpResponseNotFound


class MyFormMixin1(View):

    def dispatch(self, request, *args, **kwargs):
        #################### РЕАЛИЗУЕМ ПОЛУЧЕНИЕ ЗАЯВКИ ОТ ПОЛЬЗОВАТЕЛЯ: ####################
        if request.method == 'POST' and 'feedback1' in request.POST:
            feedback_form = FeedbackForm(request.POST)
            # print(feedback_form)
            if feedback_form.is_valid():
                Feedback_name = feedback_form.cleaned_data.get('Feedback_name')
                print(Feedback_name)
                Feedback_phone = feedback_form.cleaned_data.get('Feedback_phone')
                print(Feedback_phone)
                try:
                    # send_mail(F'Вам поступила заявка от ***[[ ТЕСТ ]]*** с абонентским номером << +7 (999) 999-99-99 >>', F'***[[ ТЕСТ ]]*** с абонентским номером << +7 (999) 999-99-99 >> отправил Вам заявку на консультацию!', 'avitadentedgar@yandex.ru', ['garrip91@mail.ru'], fail_silently=False)
                    send_mail(F'Вам поступила заявка от ***[[ {Feedback_name} ]]*** с абонентским номером << {Feedback_phone} >>', F'***[[ {Feedback_name} ]]*** с абонентским номером << {Feedback_phone} >> отправил (-а) Вам заявку на консультацию!', 'avitadentedgar@yandex.ru', ['avitadentedgar@yandex.ru'], fail_silently=False)
                    print(send_mail)
                except:
                    return HttpResponseNotFound('<h1>Письмо не отправлено</h1>')
                else:
                    print("ВАША ЗАЯВКА УСПЕШНО ОТПРАВЛЕНА!")
                    messages.success(request, "ВАША ЗАЯВКА УСПЕШНО ОТПРАВЛЕНА!")
                    feedback_form.save()
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
            if appointment_form.is_valid():
                Appointment_name = appointment_form.cleaned_data.get('Appointment_name')
                print(Appointment_name)
                Appointment_phone = appointment_form.cleaned_data.get('Appointment_phone')
                print(Appointment_phone)
                Appointment_email = appointment_form.cleaned_data.get('Appointment_email')
                print(Appointment_email)
                try:
                    # send_mail(F'Вам поступила заявка от ***[[ {Appointment_name} ]]*** с абонентским номером << {Appointment_phone} >>', F'***[[ {Appointment_name} ]]*** с абонентским номером << {Appointment_phone} >>  и почтовым адресом << {Appointment_email} >> отправил Вам заявку на запись на приём!', 'avitadentedgar@yandex.ru', ['garrip91@mail.ru'], fail_silently=False)
                    send_mail(F'Вам поступила заявка от ***[[ {Appointment_name} ]]*** с абонентским номером << {Appointment_phone} >>', F'***[[ {Appointment_name} ]]*** с абонентским номером << {Appointment_phone} >>  и почтовым адресом << {Appointment_email} >> отправил Вам заявку на запись на приём!', 'avitadentedgar@yandex.ru', ['avitadentedgar@yandex.ru'], fail_silently=False)
                    print(send_mail)
                except:
                    return HttpResponseNotFound('<h1>Письмо не отправлено</h1>')
                else:
                    print("ВАША ЗАЯВКА УСПЕШНО ОТПРАВЛЕНА!")
                    messages.success(request, "ВАША ЗАЯВКА УСПЕШНО ОТПРАВЛЕНА!")
                    appointment_form.save()
                    return HttpResponseRedirect(F'{self.request.path}#thanks')
            else:
                print("ЧТО-ТО ПОШЛО НЕ ТАК!")
                messages.error(request, 'НЕПРАВИЛЬНО ВВЕДЁН НОМЕР ТЕЛЕФОНА!')
                return HttpResponseRedirect(self.request.path)
        else:
            self.appointment_form = AppointmentForm()
        #####################################################################################
        # print(F'request.path == {request.path}')
        return super().dispatch(request, *args, **kwargs)


class MyFormMixin3(View):

    def dispatch(self, request, *args, **kwargs):
        #################### РЕАЛИЗУЕМ ПОЛУЧЕНИЕ ЗАЯВКИ ОТ ПОЛЬЗОВАТЕЛЯ: ####################
        if request.method == 'POST' and 'feedback3' in request.POST:
            footer_feedback_form = FooterFeedbackForm(request.POST)
            print(footer_feedback_form)
            if footer_feedback_form.is_valid():
                footer_feedback_form.save()
                FooterFeedback_name = footer_feedback_form.cleaned_data.get('FooterFeedback_name')
                print(FooterFeedback_name)
                FooterFeedback_phone = footer_feedback_form.cleaned_data.get('FooterFeedback_phone')
                print(FooterFeedback_phone)
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
            self.footer_feedback_form = FooterFeedbackForm()
        #####################################################################################
        # print(F'request.path == {request.path}')
        return super().dispatch(request, *args, **kwargs)