from django.conf import settings


def allauth(request):
    return {'ALLAUTH': 'allauth' in settings.INSTALLED_APPS}