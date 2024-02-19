from django import forms
from .models import Grossesse
from .models import WeightWoman

class PregnantWomanForm(forms.ModelForm):
    class Meta:
        model = WeightWoman
        fields = ['weight', 'blood_pressure']

class GrossesseForm(forms.ModelForm):
    start_date = forms.DateField(required=True,label='start_date')

    class Meta:
        model = Grossesse
        fields = ['start_date']
    