from django.db import models

# Create your models here.


class LoginTable(models.Model):
    Username=models.CharField(max_length=30, null=True, blank=True)
    Password=models.CharField(max_length=30, null=True, blank=True)
    UserType=models.CharField(max_length=30, null=True, blank=True)

class DoctorTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    Name=models.CharField(max_length=30, null=True, blank=True)
    PhNumber=models.BigIntegerField( null=True, blank=True)
    Specialization=models.CharField(max_length=30, null=True, blank=True)
    HospitalName=models.CharField(max_length=30, null=True, blank=True)
    Email=models.CharField(max_length=30, null=True, blank=True)

class PatientTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    Name=models.CharField(max_length=30, null=True, blank=True)
    Age=models.IntegerField(null=True, blank=True)
    Gender=models.CharField(max_length=30, null=True, blank=True)
    PhNumber=models.BigIntegerField( null=True, blank=True)
    Email=models.CharField(max_length=30, null=True, blank=True)
    Address=models.CharField(max_length=100, null=True, blank=True)

class AppoinmentTable(models.Model):
    PATIENT=models.ForeignKey(PatientTable, on_delete=models.CASCADE)
    DOCTOR=models.ForeignKey(DoctorTable, on_delete=models.CASCADE)
    Date=models.DateField( null=True, blank=True)
    Status=models.CharField(max_length=100, null=True, blank=True)

class MedicineTable(models.Model):
    Medicine=models.CharField(max_length=30, null=True, blank=True)
    Description=models.CharField(max_length=30, null=True, blank=True)
    Quantity=models.IntegerField(null=True, blank=True)
    Price=models.FloatField( null=True, blank=True)

class PrescriptionTable(models.Model):
    PATIENT=models.ForeignKey(PatientTable, on_delete=models.CASCADE)
    DOCTOR=models.ForeignKey(DoctorTable, on_delete=models.CASCADE)
    Prescription=models.CharField(max_length=300, null=True, blank=True)
    Medicine=models.ForeignKey(MedicineTable, on_delete=models.CASCADE)

class PostTable(models.Model):
    DOCTOR=models.ForeignKey(DoctorTable, on_delete=models.CASCADE)
    Image=models.FileField(null=True, blank=True)
    Document=models.CharField(max_length=30, null=True, blank=True)
    Date=models.DateField( null=True, blank=True)
    