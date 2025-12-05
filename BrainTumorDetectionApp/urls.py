"""
URL configuration for BrainTumorDetection project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from BrainTumorDetectionApp.views import *

urlpatterns = [
    path('', LoginPage.as_view(), name="LoginPage"),

    # //////////////////////////////////////////// ADMIN /////////////////////////////////////////////////

    path('Managedoc', ManageDoctorPage.as_view(), name="Managedoc"),
    path('manage_medi', ManageMedicinePage.as_view(), name="manage_medi"),
    path('delete_medi/<int:m_id>', DeletemedicinePage.as_view(), name="delete_medi"),
    path('edit_medi/<int:m_id>', EditmedicinePage.as_view(), name="edit_medi"),
    path('registration', RegistrationPage.as_view(), name="registration"),
    path('appoinment', viewappoinmentPage.as_view(), name="appoinment"),
    path('delete_appoinment/<int:id>', DeleteappoinmentPage.as_view(), name="delete_appoinment"),

    path('doctor', viewdoctorPage.as_view(), name="doctor"),
    path('edit_doc/<int:d_id>', EditdoctorPage.as_view(), name="edit_doc"),
    path('delete_doc/<int:d_id>', DeletedoctorPage.as_view(), name="delete_doc"),
    path('delete_patient/<int:id>', DeletepatientPage.as_view(), name="delete_patient"),
    path('medicine', medicinePage.as_view(), name="medicine"),
    path('patient', PatientPage.as_view(), name="patient"),
    path('adminhome', AdminHome.as_view(), name="adminhome"),

    # //////////////////////////////////////////// DOCTOR ////////////////////////////////////////////////

    path('notification', notificationPage.as_view(), name="notification"),
    path('post', postPage.as_view(), name="post"),
    path('prescrip', prescriptionPage.as_view(), name="prescrip"),
    path('delete_prescrip/<int:p_id>', DeleteprescriptionPage.as_view(), name="delete_prescrip"),
    path('manage_prescrip', ManageprescriptionPage.as_view(), name="manage_prescrip"),

    path('accept_reject_appoinment', acceptrejectappoinmentPage.as_view(), name="aaccept_reject_appoinment"),
    path('doctorhome', DoctorHome.as_view(), name="doctorhome"),
    path('manage', ManagePost.as_view(), name="manage"),

]
