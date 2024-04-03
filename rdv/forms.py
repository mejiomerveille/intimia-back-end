from django import forms
from .models import RendezVous as Appointment


class AppointmentForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    class Meta:
        model = Appointment
        fields = ['grossesse','doctor','date', 'time', 'reminder', 'notes']

    



class UploadFileForm(forms.Form):
    file = forms.FileField()
    title = forms.CharField(label='Titre du fichier')

# PROFESSION_CHOICES = [
    #     ('Medecin', 'Medecin'),
    #     ('Gynecologue', 'Gynecologue'),
    #     ('Visiteur medical', 'Visiteur medical'),
    #     ('Sage-femme', 'Sage-femme'),
    #     ('Infirmiere', 'Infirmiere'),
    #     ('Obstetricien', 'Obstetricien'),
    #     ('Autre', 'Autre'),
    #     ('Pediatre', 'Pediatre'),
    #     ('Kinesitherapeute', 'Kinesitherapeute'),
    #     ('Echographiste', 'Echographiste'),
    # ]

    # profession = forms.ChoiceField(choices=PROFESSION_CHOICES)
# class DoctorForm(forms.ModelForm):