from django.shortcuts import render

from django.views import View
from .models import Services, Actions, Gallery, Reviews, Orthodontics, Implantology, FunctionalDentistry, Orthopedics, Periodontology, Therapy, Surgery, Doctors
from .forms import FeedbackForm, AppointmentForm, FooterFeedbackForm

from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .mixins import MyFormMixin1, MyFormMixin2, MyFormMixin3
from django.contrib.messages.views import SuccessMessageMixin

from django.core.mail import send_mail



# Create your views here.
###### ДЛЯ ПРОВЕРКИ: ######
class TestView(View):
    def post(self, request, *args, **kwargs):
        send_mail(F'Вам поступила заявка от ***[[ ТЕСТ ]]*** с абонентским номером << +7 (999) 999-99-99 >>', F'***[[ ТЕСТ ]]*** с абонентским номером << +7 (999) 999-99-99 >> отправил Вам заявку на консультацию!', 'avitadentedgar@yandex.ru', ['garrip91@mail.ru'], fail_silently=False)
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/home.html',
            {
                'services': services,
                'form1': form1,
                'form3': form3
            }
        )
###########################


# class FeedbackFormView(View):

    # form_class = FeedbackForm
    # initial = {'key': 'value'}
    # template_name = 'feedback_form_template.html'
    # ###### ВРЕМЕННО: ######
    # def get(self, request, *args, **kwargs):
        # form = self.form_class(request.GET)
        # ###### ВРЕМЕННО: ######
        # print(F'request.path == {self.request.path}')
        # #######################
        # return render(request, self.template_name, {'form': form})
    # #######################
    # def post(self, request, *args, **kwargs):
        # form = self.form_class(request.POST)
        # print(form)
        # ###### ВРЕМЕННО: ######
        # print(F'request.path == {self.request.path}')
        # #######################
        # if form.is_valid():
            # pass
            # #return HttpResponseRedirect('/success/')
        # return render(request, self.template_name, {'form': form})


class HomePageView(MyFormMixin1, MyFormMixin3, SuccessMessageMixin, View):

    # def get(self, request):
        # #user_form = UserForm()
        # print(F'request.path == {self.request.path}')
        # return render(request, 'AvitaDentApp/home.html', context={})
    
    form_class1 = FeedbackForm
    form_class3 = FooterFeedbackForm
    def get(self, request, *args, **kwargs):
        form1 = self.form_class1(request.POST)
        form3 = self.form_class3(request.POST)
        services = Services.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/home.html',
            {
                'services': services,
                'form1': form1,
                'form3': form3
            }
        )


class ServicesPageView(MyFormMixin1, MyFormMixin3, SuccessMessageMixin, View):

    form_class1 = FeedbackForm
    form_class3 = FooterFeedbackForm
    def get(self, request, *args, **kwargs):
        form1 = self.form_class1(request.POST)
        form3 = self.form_class3(request.POST)
        services = Services.objects.all()[:25]
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/services.html',
            {
                'services': services,
                'form1': form1,
                'form3': form3
            }
        )


class ActionsPageView(MyFormMixin1, MyFormMixin3, SuccessMessageMixin, View):

    form_class1 = FeedbackForm
    form_class3 = FooterFeedbackForm
    def get(self, request, *args, **kwargs):
        form1 = self.form_class1(request.POST)
        form3 = self.form_class3(request.POST)
        actions = Actions.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/actions.html',
            {
                'actions': actions,
                'form1': form1,
                'form3': form3
            }
        )


class GalleryPageView(MyFormMixin1, MyFormMixin3, SuccessMessageMixin, View):

    form_class1 = FeedbackForm
    form_class3 = FooterFeedbackForm
    def get(self, request, *args, **kwargs):
        form1 = self.form_class1(request.POST)
        form3 = self.form_class3(request.POST)
        gallery = Gallery.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/gallery.html',
            {
                'gallery': gallery,
                'form1': form1,
                'form3': form3
            }
        )


class ClinicPageView(MyFormMixin1, MyFormMixin3, SuccessMessageMixin, View):

    form_class1 = FeedbackForm
    form_class3 = FooterFeedbackForm
    def get(self, request, *args, **kwargs):
        form1 = self.form_class1(request.POST)
        form3 = self.form_class3(request.POST)
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/clinic-page.html',
            {
                'form1': form1,
                'form3': form3
            }
        )


class ReviewsPageView(MyFormMixin1, MyFormMixin3, SuccessMessageMixin, View):

    form_class1 = FeedbackForm
    form_class3 = FooterFeedbackForm
    def get(self, request, *args, **kwargs):
        form1 = self.form_class1(request.POST)
        form3 = self.form_class3(request.POST)
        reviews = Reviews.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/reviews.html',
            {
                'reviews': reviews,
                'form1': form1,
                'form3': form3
            }
        )


class ContactsPageView(MyFormMixin1, MyFormMixin2, MyFormMixin3, SuccessMessageMixin, View):

    form_class1 = FeedbackForm
    form_class2 = AppointmentForm
    form_class3 = FooterFeedbackForm
    def get(self, request, *args, **kwargs):
        form1 = self.form_class1(request.POST)
        form2 = self.form_class2(request.POST)
        form3 = self.form_class3(request.POST)
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/contacts.html',
            {
                #'reviews': reviews,
                'form1': form1,
                'form2': form2,
                'form3': form3
            }
        )


class OrthodonticsPageView(MyFormMixin1, MyFormMixin3, SuccessMessageMixin, View):

    form_class1 = FeedbackForm
    form_class3 = FooterFeedbackForm
    def get(self, request, *args, **kwargs):
        form1 = self.form_class1(request.POST)
        form3 = self.form_class3(request.POST)
        orthodontics = Orthodontics.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/orthodontics.html',
            {
                'orthodontics': orthodontics,
                'form1': form1,
                'form3': form3
            }
        )


class ImplantologyPageView(MyFormMixin1, MyFormMixin3, SuccessMessageMixin, View):

    form_class1 = FeedbackForm
    form_class3 = FooterFeedbackForm
    def get(self, request, *args, **kwargs):
        form1 = self.form_class1(request.POST)
        form3 = self.form_class3(request.POST)
        implantology = Implantology.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/implantology.html',
            {
                'implantology': implantology,
                'form1': form1,
                'form3': form3
            }
        )


class FunctionalDentistryPageView(MyFormMixin1, MyFormMixin3, SuccessMessageMixin, View):

    form_class1 = FeedbackForm
    form_class3 = FooterFeedbackForm
    def get(self, request, *args, **kwargs):
        form1 = self.form_class1(request.POST)
        form3 = self.form_class3(request.POST)
        functional_dentistry = FunctionalDentistry.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/functional-dentistry.html',
            {
                'functional_dentistry': functional_dentistry,
                'form1': form1,
                'form3': form3
            }
        )


class OrthopedicsPageView(MyFormMixin1, MyFormMixin3, SuccessMessageMixin, View):

    form_class1 = FeedbackForm
    form_class3 = FooterFeedbackForm
    def get(self, request, *args, **kwargs):
        form1 = self.form_class1(request.POST)
        form3 = self.form_class3(request.POST)
        orthopedics = Orthopedics.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/orthopedics.html',
            {
                'orthopedics': orthopedics,
                'form1': form1,
                'form3': form3
            }
        )


class PeriodontologyPageView(MyFormMixin1, MyFormMixin3, SuccessMessageMixin, View):

    form_class1 = FeedbackForm
    form_class3 = FooterFeedbackForm
    def get(self, request, *args, **kwargs):
        form1 = self.form_class1(request.POST)
        form3 = self.form_class3(request.POST)
        periodontology = Periodontology.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/periodontology.html',
            {
                'periodontology': periodontology,
                'form1': form1,
                'form3': form3
            }
        )


class TherapyPageView(MyFormMixin1, MyFormMixin3, SuccessMessageMixin, View):

    form_class1 = FeedbackForm
    form_class3 = FooterFeedbackForm
    def get(self, request, *args, **kwargs):
        form1 = self.form_class1(request.POST)
        form3 = self.form_class3(request.POST)
        therapy = Therapy.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/therapy.html',
            {
                'therapy': therapy,
                'form1': form1,
                'form3': form3
            }
        )


class SurgeryPageView(MyFormMixin1, MyFormMixin3, SuccessMessageMixin, View):

    form_class1 = FeedbackForm
    form_class3 = FooterFeedbackForm
    def get(self, request, *args, **kwargs):
        form1 = self.form_class1(request.POST)
        form3 = self.form_class3(request.POST)
        surgery = Surgery.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/surgery.html',
            {
                'surgery': surgery,
                'form1': form1,
                'form3': form3
            }
        )


class CertificatesAndLicensesPageView(MyFormMixin1, MyFormMixin3, SuccessMessageMixin, View):

    form_class1 = FeedbackForm
    form_class3 = FooterFeedbackForm
    def get(self, request, *args, **kwargs):
        form1 = self.form_class1(request.POST)
        form3 = self.form_class3(request.POST)
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/certificates-and-licenses.html',
            {
                'form1': form1,
                'form3': form3
            }
        )


class PrivacyPolicyPageView(MyFormMixin1, MyFormMixin3, SuccessMessageMixin, View):

    form_class1 = FeedbackForm
    form_class3 = FooterFeedbackForm
    def get(self, request, *args, **kwargs):
        form1 = self.form_class1(request.POST)
        form3 = self.form_class3(request.POST)
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/privacy-policy.html',
            {
                'form1': form1,
                'form3': form3
            }
        )