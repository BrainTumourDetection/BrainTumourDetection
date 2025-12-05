from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from BrainTumorDetectionApp.forms import DoctorForm, MedicineForms, PrescriptionForms
from BrainTumorDetectionApp.models import AppoinmentTable, DoctorTable, LoginTable, MedicineTable, PatientTable, PostTable, PrescriptionTable, notificationTable

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
        if request.method == 'POST':
            print("-------------------->", request.POST)

            form = DoctorForm(request.POST)
            username = request.POST['Email']
            password = request.POST['password']
            login_obj = LoginTable(Username=username, Password=password, UserType='doctor')
            login_obj.save()
            print("----------------", request.POST)
            if form.is_valid():
                f=form.save(commit=False)
                f.LOGIN=login_obj
                f.save()
                return redirect('doctor')


class EditdoctorPage(View):
    def get(self, request, d_id):
        obj = DoctorTable.objects.get(id=d_id)
        return render(request, "administration/edit_doc.html", {'val': obj})
    def post(self, request,d_id):
        if request.method == 'POST':
            obj = DoctorTable.objects.get(id=d_id)
            form = DoctorForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('doctor')

class DeletedoctorPage(View):
    def get(self, request, d_id):
        obj = LoginTable.objects.get(id=d_id)
        obj.delete()
        return redirect('doctor')
    
class DeletepatientPage(View):
    def get(self, request, id):
        obj = LoginTable.objects.get(id=id)
        obj.delete()
        return redirect('patient')

class ManageMedicinePage(View):
    def get(self, request):
        return render(request, "administration/manage_medi.html")
    def post(self, request):
        v=MedicineForms(request.POST)
        if v.is_valid():
            v.save()
            return redirect('medicine')
        
class DeletemedicinePage(View):
    def get(self, request, m_id):
        obj = MedicineTable.objects.get(id=m_id)
        obj.delete()
        return redirect('medicine')
    
class EditmedicinePage(View):
    def get(self, request, m_id):
        obj = MedicineTable.objects.get(id=m_id)
        return render(request, "administration/edit_medi.html", {'val': obj})
    def post(self, request,m_id):
        if request.method == 'POST':
            obj = MedicineTable.objects.get(id=m_id)
            form = MedicineForms(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('medicine')


class RegistrationPage(View):
    def get(self, request):
        return render(request, "administration/registration.html")
    
class viewappoinmentPage(View):
    def get(self, request):
        obj = AppoinmentTable.objects.all()
        return render(request, "administration/view_appoinment.html", {'val': obj} )
class DeleteappoinmentPage(View):
    def get(self, request, id):
        obj = AppoinmentTable.objects.get(id=id)
        obj.delete()
        return redirect('appoinment')
    
class viewdoctorPage(View):
    def get(self, request):
        obj = DoctorTable.objects.all()
        return render(request, "administration/view_doctor.html", {'val': obj} )
class medicinePage(View):
    def get(self, request):
        obj = MedicineTable.objects.all()
        return render(request, "administration/view_medi.html", {'val': obj})
class PatientPage(View):
    def get(self, request):
        obj = PatientTable.objects.all()
        return render(request, "administration/view_patient.html", {'val': obj})
    
class AdminHome(View):
    def get(self, request):
        return render(request, "administration/admin_dashboard.html")  
    
# ////////////////////////////////////////// DOCTOR /////////////////////////////////////////////////

class notificationPage(View):
    def get(self, request):
        obj = notificationTable.objects.all()
        return render(request, "doctor/notification.html", {'val': obj} )
    
class postPage(View):
    def get(self, request):
        obj = PostTable.objects.all()
        return render(request, "doctor/post_table.html", {'val': obj} )
    
class prescriptionPage(View):
    def get(self, request):
        obj = PrescriptionTable.objects.all()
        return render(request, "doctor/prescription.html", {'val': obj} )
class DeleteprescriptionPage(View):
    def get(self, request,p_id):
        obj = PrescriptionTable.objects.get(id=p_id)
        obj.delete()
        return redirect('prescrip')
class ManageprescriptionPage(View):
    def get(self, request):
        return render(request, "doctor/manage_prescrip.html")
    def post(self, request):
        v=PrescriptionForms(request.POST)
        if v.is_valid():
            v.save()
            return redirect('prescrip')

class acceptrejectappoinmentPage(View):
    def get(self, request):
        obj = AppoinmentTable.objects.all()
        return render(request, "doctor/accept_reject_appoinment.html", {'val': obj} )
    
class DoctorHome(View):
    def get(self, request):
        return render(request, "doctor/doctor_dashboard.html")
    
class ManagePost(View):
    def get(self, request):
        obj = PostTable.objects.all()
        return render(request, "doctor/manage_post.html", {'val': obj} )