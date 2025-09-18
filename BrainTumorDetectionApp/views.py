from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from BrainTumorDetectionApp.forms import DoctorForm
from BrainTumorDetectionApp.models import LoginTable

# Create your views here.

class LoginPage(View):
    def get(self, request):
        return render(request, "login.html")
    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            obj=LoginTable.objects.get(Username=username, Password=password)
            request.session['user_id'] = obj.id
            if obj.UserType == 'admin':
                return HttpResponse("<script>alert('Login successful');window.location='/adminhome'</script>")
            elif obj.UserType == 'doctor':
                return HttpResponse("<script>alert('Login successful');window.location='/doctorhome'</script>")
            
        except LoginTable.DoesNotExist:
                return HttpResponse("<script>alert('Invalid username or password');window.location='/login'</script>")
            
    

# /////////////////////////////////////////////////////// ADMIN ///////////////////////////////////////////
#     
class ManageDoctorPage(View):
    def get(self, request):
        return render(request, "administration/manage_doc.html")
    def post(self, request):
        if request.method == 'POST' and request.FILES:
            print("-------------------->", request.POST)
            form = DoctorForm(request.POST, request.FILES)
            username = request.POST['username']
            password = request.POST['password']
            login_obj = LoginTable(username=username, password=password, user_type='doctor')
            login_obj.save()
            if form.is_valid():
                f=form.save(commit=False)
                f.LOGIN=login_obj
                f.save()
                return redirect('managedoctor')

class ManageMedicinePage(View):
    def get(self, request):
        return render(request, "administration/manage_medi.html")
class RegistrationPage(View):
    def get(self, request):
        return render(request, "administration/registration.html")
class viewappoinmentPage(View):
    def get(self, request):
        return render(request, "administration/view_appoinment.html")
class viewdoctorPage(View):
    def get(self, request):
        return render(request, "administration/view_doctor.html")
class medicinePage(View):
    def get(self, request):
        return render(request, "administration/view-medi.html")
class PatientPage(View):
    def get(self, request):
        return render(request, "administration/view_patient.html")
class AdminHome(View):
    def get(self, request):
        return render(request, "administration/admin_dashboard.html")  

# ////////////////////////////////////////// DOCTOR /////////////////////////////////////////////////

class notificationPage(View):
    def get(self, request):
        return render(request, "doctor/notification.html")
class postPage(View):
    def get(self, request):
        return render(request, "doctor/post_table.html")
class prescriptionPage(View):
    def get(self, request):
        return render(request, "doctor/prescription.html")
class acceptrejectappoinmentPage(View):
    def get(self, request):
        return render(request, "doctor/accept_reject_appoinment.html")
class DoctorHome(View):
    def get(self, request):
        return render(request, "doctor/doctor_dashboard.html")
class ManagePost(View):
    def get(self, request):
        return render(request, "doctor/manage_post.html")