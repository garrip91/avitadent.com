from django.shortcuts import render

from django.views import View
from .models import Actions, Services
from .forms import FeedbackForm



# Create your views here.
###### ДЛЯ ПРОВЕРКИ: ######
#class BaseView(View):
###########################


class FeedbackFormView(View):

    form_class = FeedbackForm
    initial = {'key': 'value'}
    template_name = 'feedback_form_template.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            pass
            #return HttpResponseRedirect('/success/')
        return render(request, self.template_name, {'form': form})


class HomePageView(View):

    # def get(self, request):
        # #user_form = UserForm()
        # print(F'request.path == {self.request.path}')
        # return render(request, 'AvitaDentApp/home.html', context={})
        
    def get(self, request, *args, **kwargs):
        services = Services.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/home.html',
            {
                'services': services,
            }
        )
        
        
class ServicesPageView(View):

    def get(self, request):
        #user_form = UserForm()
        print(F'request.path == {self.request.path}')
        return render(request, 'AvitaDentApp/services.html', context={})


class ActionsPageView(View):

    # template_name = 'AvitaDentApp/actions.html'

    # def get(self, request):
        # #user_form = UserForm()
        # print(F'request.path == {self.request.path}')
        # return render(request, 'AvitaDentApp/actions.html', context={})

    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context['actions'] = Actions.objects.all()
        # return context
        
    def get(self, request, *args, **kwargs):
        actions = Actions.objects.all()
        print(F'request.path == {self.request.path}')
        return render(
            request,
            'AvitaDentApp/actions.html',
            {
                'actions': actions,
            }
        )


class GalleryPageView(View):

    def get(self, request):
        #user_form = UserForm()
        print(F'request.path == {self.request.path}')
        return render(request, 'AvitaDentApp/gallery.html', context={})


class ClinicPageView(View):

    def get(self, request):
        #user_form = UserForm()
        print(F'request.path == {self.request.path}')
        return render(request, 'AvitaDentApp/clinic-page.html', context={})


class ReviewsPageView(View):

    def get(self, request):
        #user_form = UserForm()
        print(F'request.path == {self.request.path}')
        return render(request, 'AvitaDentApp/reviews.html', context={})


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