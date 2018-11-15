from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django_redis import get_redis_connection
from django.http import HttpResponse
from rest_framework.views import APIView
from . import constants
from rest_framework.generics import GenericAPIView
from .serializers import RegisterSmscodeSerializer
from random import randint
from rest_framework.response import Response
from .constants import CODE_EFFECTIVE_TIME
from rest_framework import status
from libs.yuntongxun import CCP


# Create your views here.
# 短信验证
class RegisterSmscodeView(GenericAPIView):

    serializer_class = RegisterSmscodeSerializer

    def get(self, request, phone):
        # 1. 手机号
        params = request.query_params

        # 2.  对用户输入的 图片验证码进行校验
        serializer = self.get_serializer(data=params)
        serializer.is_valid(raise_exception=True)

        # 3.  生成短信

        sms_code = '%06d'%randint(0,999999)

        # 3.1 将短信记录在redis中
        redis_conn = get_redis_connection('code')

        # 3.2 需要先判断 有没有给用户发送过
        flag = redis_conn.get('sms_flag_%s'%phone)
        if flag:
            return Response(status=status.HTTP_429_TOO_MANY_REQUESTS)

        redis_conn.setex('sms_%s'%phone,CODE_EFFECTIVE_TIME*5,sms_code)

        # 3.3 记录一个标记,
        redis_conn.setex('sms_flag_%s'%phone,60,1)


        # 4. 发送短信

        ccp = CCP()
        ccp.send_template_sms(phone,[sms_code,5],1)

        #from celery_tasks.sms.tasks import send_sms_code

        # 方法调用的通过delay
        # 要给函数传递的参数 是通过 delay 来实现传递的
        #send_sms_code.delay(phone,sms_code)

        return Response({'message':'ok'})
