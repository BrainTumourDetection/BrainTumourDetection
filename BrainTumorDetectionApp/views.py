from django.shortcuts import render
from django.views import View

# Create your views here.

class LoginPage(View):
    def get(self, request):
        return render(request, "login.html")
class ManageDoctorPage(View):
    def get(self, request):
        return render(request, "administration/manage doc.html")
class ManageMedicinePage(View):
    def get(self, request):
        return render(request, "administration/manage medi.html")
class RegistrationPage(View):
    def get(self, request):
        return render(request, "administration/registration.html")
class viewappoinmentPage(View):
    def get(self, request):
        return render(request, "administration/view appoinment.html")
class viewdoctorPage(View):
    def get(self, request):
        return render(request, "administration/view doctor.html")
class medicinePage(View):
    def get(self, request):
        return render(request, "administration/view medi.html")
class PatientPage(View):
    def get(self, request):
        return render(request, "administration/view patient.html")
class notificationPage(View):
    def get(self, request):
        return render(request, "doctor/notification.html")
class postPage(View):
    def get(self, request):
        return render(request, "doctor/post table.html")
class prescriptionPage(View):
    def get(self, request):
        return render(request, "doctor/prescription.html")
class viewappoinmentPage(View):
    def get(self, request):
        return render(request, "doctor/view appoinment.html")
