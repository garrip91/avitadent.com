from .models import Doctors, Instagram_Links, Certificates
from .forms import FeedbackForm



def get_doctors_data(request):

    doctors = Doctors.objects.all()
    return {'doctors': doctors}


# def get_feedback_data(request):

    # form_class = FeedbackForm
    # form = self.form_class(request.POST)
    # return {'form': form}


# def get_instagram_links_data(request):

    # instagram_links = Instagram_Links.objects.all()
    # return {'instagram_links': instagram_links}


def get_certificates_data(request):

    certificates = Certificates.objects.all()
    return {'certificates': certificates}