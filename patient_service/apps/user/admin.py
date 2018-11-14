from django.contrib import admin
from .models import User, Patient, Doctor, Enterprise

# Register your models here.

admin.site.site_header = '全国患者服务系统后台管理'