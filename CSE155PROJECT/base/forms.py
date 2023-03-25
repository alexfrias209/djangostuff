from django.forms import ModelForm
from .models import Room, Account, UserProfile, MultipleImage

class uploadForm(ModelForm):
    class Meta:
        model = Account
        fields = ['username']