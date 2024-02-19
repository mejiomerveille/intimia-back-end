from django import forms
from .models import RDV as Appointment,Doctor


class AppointmentForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    PROFESSION_CHOICES = [
        ('Medecin', 'Medecin'),
        ('Gynecologue', 'Gynecologue'),
        ('Visiteur medical', 'Visiteur medical'),
        ('Sage-femme', 'Sage-femme'),
        ('Infirmiere', 'Infirmiere'),
        ('Obstetricien', 'Obstetricien'),
        ('Autre', 'Autre'),
        ('Pediatre', 'Pediatre'),
        ('Kinesitherapeute', 'Kinesitherapeute'),
        ('Echographiste', 'Echographiste'),
    ]

    profession = forms.ChoiceField(choices=PROFESSION_CHOICES)

    class Meta:
        model = Appointment
        fields = ['name','profession','email','date', 'time', 'weight', 'reminder', 'notes']

# class DoctorForm(forms.ModelForm):
    



class UploadFileForm(forms.Form):
    file = forms.FileField()
    title = forms.CharField(label='Titre du fichier')