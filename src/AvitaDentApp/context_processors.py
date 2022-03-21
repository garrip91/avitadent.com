from .models import Doctors



def get_doctors_data(request):

    doctors = Doctors.objects.all()
    
    return {'doctors': doctors}