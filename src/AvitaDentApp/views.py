from django.shortcuts import render

from django.views import View
from .models import Services, Actions, Gallery, Reviews, Orthodontics, Implantology, FunctionalDentistry, Orthopedics, Periodontology, Therapy, Surgery, Doctors
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
        
    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context['doctors'] = Doctors.objects.all()
        # return context
        
        
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


class OrthodonticsPageView(MyFormMixin, SuccessMessageMixin, View):

    form_class = FeedbackForm
    def get(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        orthodontics = Orthodontics.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/orthodontics.html',
            {
                'orthodontics': orthodontics,
                'form': form
            }
        )


class ImplantologyPageView(MyFormMixin, SuccessMessageMixin, View):

    form_class = FeedbackForm
    def get(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        implantology = Implantology.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/implantology.html',
            {
                'implantology': implantology,
                'form': form
            }
        )


class FunctionalDentistryPageView(MyFormMixin, SuccessMessageMixin, View):

    form_class = FeedbackForm
    def get(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        functional_dentistry = FunctionalDentistry.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/functional-dentistry.html',
            {
                'functional_dentistry': functional_dentistry,
                'form': form
            }
        )


class OrthopedicsPageView(MyFormMixin, SuccessMessageMixin, View):

    form_class = FeedbackForm
    def get(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        orthopedics = Orthopedics.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/orthopedics.html',
            {
                'orthopedics': orthopedics,
                'form': form
            }
        )


class PeriodontologyPageView(MyFormMixin, SuccessMessageMixin, View):

    form_class = FeedbackForm
    def get(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        periodontology = Periodontology.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/periodontology.html',
            {
                'periodontology': periodontology,
                'form': form
            }
        )


class TherapyPageView(MyFormMixin, SuccessMessageMixin, View):

    form_class = FeedbackForm
    def get(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        therapy = Therapy.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/therapy.html',
            {
                'therapy': therapy,
                'form': form
            }
        )


class SurgeryPageView(MyFormMixin, SuccessMessageMixin, View):

    form_class = FeedbackForm
    def get(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        surgery = Surgery.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/surgery.html',
            {
                'surgery': surgery,
                'form': form
            }
        )


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