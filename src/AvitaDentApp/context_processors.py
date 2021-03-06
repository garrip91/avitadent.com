from .models import Doctors, Certificates, Licenses, Instagram_Links, Actions, Reviews
from .forms import FeedbackForm



def get_doctors_data(request):

    doctors = Doctors.objects.all()
    return {'doctors': doctors}


# def get_feedback_data(request):

    # form_class = FeedbackForm
    # form = self.form_class(request.POST)
    # return {'form': form}


def get_certificates_data(request):

    certificates = Certificates.objects.all()
    return {'certificates': certificates}


def get_licenses_data(request):

    licenses = Licenses.objects.all()
    return {'licenses': licenses}


def get_instagram_links_data(request):

    links = Instagram_Links.objects.all()
    return {'links': links}


def get_actions_data(request):

    actions = Actions.objects.all()
    return {'actions': actions}


def get_reviews_data(request):

    reviews = Reviews.objects.all()
    return {'reviews': reviews}