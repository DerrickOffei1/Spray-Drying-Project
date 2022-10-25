from django import forms
from .  models import Database

class DataForm(forms.ModelForm):
    class Meta:
        model = Database
        fields = ['Temperature', 'Maltodextrin', 'FlowRate']