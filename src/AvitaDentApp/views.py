from django.shortcuts import render

from django.views import View



# Create your views here.
class HomePageView(View):

    def get(self, request):
        #user_form = UserForm()
        print(F'request.path == {self.request.path}')
        return render(request, 'AvitaDentApp/home.html', context={})