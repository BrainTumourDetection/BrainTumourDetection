from django.contrib import admin

from BrainTumorDetectionApp.models import AppoinmentTable, DoctorTable, LoginTable, MedicineTable, PatientTable, PostTable, PrescriptionTable, notificationTable

# Register your models here.
admin.site.register(LoginTable)
admin.site.register(DoctorTable)
admin.site.register(PatientTable)
admin.site.register(AppoinmentTable)
admin.site.register(MedicineTable)
admin.site.register(PrescriptionTable)
admin.site.register(PostTable)
admin.site.register(notificationTable)