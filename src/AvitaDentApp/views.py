from django.shortcuts import render

from django.views import View
from .models import Services, Actions, Gallery, Reviews
from .forms import FeedbackForm

from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .mixins import MyFormMixin
from django.contrib.messages.views import SuccessMessageMixin



# Create your views here.
###### ДЛЯ ПРОВЕРКИ: ######
class TestView(View):

    def get(self, request):
        #user_form = UserForm()
        print(F'request.path == {self.request.path}')
        #return render(request, 'test.html', context={})
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER/test/'))
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


class HomePageView(MyFormMixin, SuccessMessageMixin, View):

    # def get(self, request):
        # #user_form = UserForm()
        # print(F'request.path == {self.request.path}')
        # return render(request, 'AvitaDentApp/home.html', context={})
    
    form_class = FeedbackForm
    def get(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        services = Services.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/home.html',
            {
                'services': services,
                'form': form
            }
        )
        
        
class ServicesPageView(MyFormMixin, SuccessMessageMixin, View):

    form_class = FeedbackForm
    def get(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        services = Services.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/services.html',
            {
                'services': services,
                'form': form
            }
        )


class ActionsPageView(MyFormMixin, SuccessMessageMixin, View):

    form_class = FeedbackForm
    def get(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        actions = Actions.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/actions.html',
            {
                'actions': actions,
                'form': form
            }
        )


class GalleryPageView(MyFormMixin, SuccessMessageMixin, View):

    form_class = FeedbackForm
    def get(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        gallery = Gallery.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/gallery.html',
            {
                'gallery': gallery,
                'form': form
            }
        )


class ClinicPageView(View):

    def get(self, request):
        #user_form = UserForm()
        print(F'request.path == {self.request.path}')
        return render(request, 'AvitaDentApp/clinic-page.html', context={})


class ReviewsPageView(MyFormMixin, SuccessMessageMixin, View):

    # def get(self, request):
        # #user_form = UserForm()
        # print(F'request.path == {self.request.path}')
        # return render(request, 'AvitaDentApp/reviews.html', context={})
    form_class = FeedbackForm
    def get(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        reviews = Reviews.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/reviews.html',
            {
                'reviews': reviews,
                'form': form
            }
        )


class ContactsPageView(View):

    def get(self, request):
        #user_form = UserForm()
        print(F'request.path == {self.request.path}')
        return render(request, 'AvitaDentApp/contacts.html', context={})


class OrthodonticsPageView(View):

    def get(self, request):
        #user_form = UserForm()
        print(F'request.path == {self.request.path}')
        return render(request, 'AvitaDentApp/orthodontics.html', context={})


class ImplantologyPageView(View):

    def get(self, request):
        #user_form = UserForm()
        print(F'request.path == {self.request.path}')
        return render(request, 'AvitaDentApp/implantology.html', context={})


class FunctionalDentistryPageView(View):

    def get(self, request):
        #user_form = UserForm()
        print(F'request.path == {self.request.path}')
        return render(request, 'AvitaDentApp/functional-dentistry.html', context={})


class OrthopedicsPageView(View):

    def get(self, request):
        #user_form = UserForm()
        print(F'request.path == {self.request.path}')
        return render(request, 'AvitaDentApp/orthopedics.html', context={})


class PeriodontologyPageView(View):

    def get(self, request):
        #user_form = UserForm()
        print(F'request.path == {self.request.path}')
        return render(request, 'AvitaDentApp/periodontology.html', context={})


class TherapyPageView(View):

    def get(self, request):
        #user_form = UserForm()
        print(F'request.path == {self.request.path}')
        return render(request, 'AvitaDentApp/therapy.html', context={})


class SurgeryPageView(View):

    def get(self, request):
        #user_form = UserForm()
        print(F'request.path == {self.request.path}')
        return render(request, 'AvitaDentApp/surgery.html', context={})


class CertificatesAndLicensesPageView(View):

    def get(self, request):
        #user_form = UserForm()
        print(F'request.path == {self.request.path}')
        return render(request, 'AvitaDentApp/certificates-and-licenses.html', context={})


class PrivacyPolicyPageView(View):

    def get(self, request):
        #user_form = UserForm()
        print(F'request.path == {self.request.path}')
        return render(request, 'AvitaDentApp/privacy-policy.html', context={})