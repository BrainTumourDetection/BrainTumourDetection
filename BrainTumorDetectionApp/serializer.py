from .models import *
from rest_framework.serializers import ModelSerializer


class LoginSerializr(ModelSerializer):
    class Meta:
        model=LoginTable
        fields='__all__'

class DoctorSerializer(ModelSerializer):
    class Meta:
        model=DoctorTable
        fields='__all__'

class PatientSerializer(ModelSerializer):
    class Meta:
        model=PatientTable
        fields='__all__'
        read_only_fields = ['LOGIN']

class AppoinmentSerializer(ModelSerializer):
    class Meta:
        model=AppoinmentTable
        fields='__all__'

class MedicineSerializer(ModelSerializer):
    class Meta:
        model=MedicineTable
        fields='__all__'

class PrescriptionSerializer(ModelSerializer):
    class Meta:
        model=PrescriptionTable
        fields='__all__'

class PostSerializer(ModelSerializer):
    class Meta:
        model=PostTable
        fields='__all__'

class NotificationSerializer(ModelSerializer):
    class Meta:
        model=notificationTable
        fields='__all__'