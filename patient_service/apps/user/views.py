from django.shortcuts import render

# Create your views here.
from django_redis import get_redis_connection
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .forms import PatientRegister, DoctorRegister, EnterPriseRegister
from .models import User, Patient, Doctor, Enterprise


# 患者注册会员
class PatientRegister(GenericAPIView):

    def get(self, request, phone):
        pass

    def post(self, request):
        register_form = PatientRegister(request.POST)
        if register_form.is_valid():
            phone = request.POST.get('phone', '')
            if Patient.objects.filter(phone=phone):
                return render(request,'')
            password = request.POST.get('password', '')
            patient_user = Patient()

