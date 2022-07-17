from django import forms
from .models import amaze

class amazeform(forms.ModelForm):
    class Meta:
        model = amaze
        fields = ("url","exp_val",)

