from app.models import Profiles
from django.forms import ModelForm


class ProfileForm(ModelForm):
    class Meta:
        model = Profiles
        exclude=['uuid']