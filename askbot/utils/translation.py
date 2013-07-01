from django.conf import settings as django_settings
from django.utils import translation

def get_language():
    if django_settings.ASKBOT_MULTILINGUAL:
        return translation.get_language()
    else:
        return django_settings.LANGUAGE_CODE

