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
    path('Managemed', ManageMedicinePage.as_view(), name="Managemed"),
    path('registration', RegistrationPage.as_view(), name="registration"),
    path('appoinment', viewappoinmentPage.as_view(), name="appoinment"),
    path('doctor', viewdoctorPage.as_view(), name="doctor"),
    path('medicine', medicinePage.as_view(), name="medicine"),
    path('patient', PatientPage.as_view(), name="patient"),
    path('adminhome', AdminHome.as_view(), name="adminhome"),

    # //////////////////////////////////////////// DOCTOR ////////////////////////////////////////////////

    path('notification', notificationPage.as_view(), name="notification"),
    path('post', postPage.as_view(), name="post"),
    path('prescrip', prescriptionPage.as_view(), name="prescrip"),
    path('accept_reject_appoinment', acceptrejectappoinmentPage.as_view(), name="aaccept_reject_appoinment"),
    path('doctorhome', DoctorHome.as_view(), name="doctorhome"),
    path('manage', ManagePost.as_view(), name="manage"),

]
