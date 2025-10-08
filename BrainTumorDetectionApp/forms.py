from django import forms
from .models import *
class DoctorForm(forms.ModelForm):
    class Meta:
        model = DoctorTable
        fields = ['Name','PhNumber','Specialization','HospitalName','Email']

class PatientForm(forms.ModelForm):
    class Meta:
        model = PatientTable
        fields = ['Name','Age','Gender','PhNumber','Email','Address']

class AppoinmentForms(forms.ModelForm):
    class Meta:
        model = AppoinmentTable
        fields = ['Date','Status']

class MedicineForms(forms.ModelForm):
    class Meta:
        model = MedicineTable
        fields = ['Medicine','Description','Quantity','Price']

class PrescriptionForms(forms.ModelForm):
    class Meta:
        model = PrescriptionTable
        fields = ['Prescription','Medicine']

class PostForms(forms.ModelForm):
    class Meta:
        model = PostTable
        fields = ['Image','Document','Date']
        