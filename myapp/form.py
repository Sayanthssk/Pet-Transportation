from django.forms import ModelForm

from .models import *


class Reply_form(ModelForm):
    class Meta:
        model = Complaint_model
        fields = ['reply']
