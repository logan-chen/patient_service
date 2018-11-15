# coding:utf8
from rest_framework import serializers
from django_redis import get_redis_connection


class RegisterSmscodeSerializer(serializers.Serializer):

    def validate(self, attrs):

        # 1. 获取用户的输入验证码
        text = attrs.get('text')
        image_code_id = attrs['image_code_id']
        # 2. 得到redis中的验证码
        redis_conn = get_redis_connection('code')

        redis_code = redis_conn.get('img_%s' % image_code_id)

        # 判断 code 是否存在
        if redis_code is None:
            raise serializers.ValidationError('验证码已过期')

        # 获取了图片验证码之后,就把图片删除
        redis_conn.delete('img_%s' % image_code_id)

        # 3. 比较
        # redis的数据类型是 bytes类型
        # 将字符串都进行小写处理
        if redis_code.decode().lower() != text.lower():
            raise serializers.ValidationError('验证码不一致')

        return attrs
