from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


# 用户模型


class User(AbstractUser):
    # 服务系统用户与患者、医生、药企多对多关系
    IDENTITY_CHOICES = (
        (0, '患者'),
        (1, '医生'),
        (2, '药企')
    )
    phone = models.CharField(max_length=11, verbose_name="手机号", unique=True)
    type_id = models.SmallIntegerField(choices=IDENTITY_CHOICES, verbose_name='用户身份', unique=True)

    class Meta:
        db_table = 'all_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


# 患者模型
class Patient(models.Model):
    # 患者和医者关系外键
    STATUS_CHOICES = (
        (0, '未通过'),
        (1, '已通过'),
        (2, '待审核')
    )
    GENDER_CHOICES = (
        (0, '男'),
        (1, '女')
    )
    recommend_id = models.ForeignKey(to="Doctor", to_field="phone", verbose_name='推荐医生', blank=True)
    name = models.CharField(max_length=10, verbose_name="姓名")
    phone = models.CharField(max_length=11, verbose_name="手机号", unique=True)
    # password = models.CharField(max_length=50, verbose_name='密码')
    pic = models.ImageField(upload_to='t_img', verbose_name="头像图片")
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    city_info = models.CharField(max_length=50, verbose_name="所在地区")
    # 病例图片
    height = models.CharField(max_length=10, verbose_name='身高')
    weight = models.CharField(max_length=6, verbose_name='体重')
    o_contact = models.CharField(max_length=20, verbose_name='其他联系方式')
    family = models.CharField(max_length=11, verbose_name='家属联系方式')
    # recommend = models.CharField(max_length=10,verbose_name="推荐医生",null=True)
    disease_info = models.CharField(max_length=50, verbose_name='具体病症')
    treatment_info = models.CharField(max_length=100, verbose_name="用药情况", blank=True)
    # 病例图片
    join = models.CharField(max_length=1, default='否', verbose_name='是否入组')
    case_img = models.ImageField(upload_to='b_img', verbose_name="病例图片")
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=2, verbose_name='用户状态审核')
    user_id = models.OneToOneField(to="User", to_field="type_id", default=0, unique=True, verbose_name='用户身份')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创新时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='审核时间')

    class Meta:
        db_table = 'pit_users'
        verbose_name = '患者信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 医生
class Doctor(models.Model):
    STATUS_CHOICES = (
        (0, '未通过'),
        (1, '已通过'),
        (2, '待审核')
    )
    GENDER_CHOICES = (
        (0, '男'),
        (1, '女')
    )
    recommend_id = models.ForeignKey('self', max_length=11, verbose_name='推荐人', blank=True)
    name = models.CharField(max_length=10, verbose_name="姓名")
    nickname = models.CharField(max_length=10, verbose_name="昵称", unique=True, blank=True)
    phone = models.CharField(max_length=11, verbose_name="手机号", unique=True)
    o_contact = models.CharField(max_length=20, verbose_name='其他联系方式')
    # password = models.CharField(max_length=50, verbose_name='密码')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    city_info = models.CharField(max_length=20, verbose_name="所在地区")
    pic = models.ImageField(upload_to='d_img', verbose_name="头像图片")
    department = models.CharField(max_length=10, verbose_name='科室')
    affiliated_hospital = models.CharField(max_length=20, verbose_name='所属医院')
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=2, verbose_name='用户状态审核')
    user_id = models.OneToOneField(to="User", to_field="type_id", default=1, unique=True, verbose_name='用户身份')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创新时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='审核时间')

    class Meta:
        db_table = 'dt_users'
        verbose_name = '医者信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 药企
class Enterprise(models.Model):
    # 企业全称，手机号，密码，姓名，邮箱，所需服务，职位，公司产品，等级，公司地址，头像）
    STATUS_CHOICES = (
        (0, '未通过'),
        (1, '已通过'),
        (2, '待审核')
    )
    e_name = models.CharField(max_length=20, verbose_name='企业名称')
    name = models.CharField(max_length=10, verbose_name="联系人姓名")
    phone = models.CharField(max_length=11, verbose_name="手机号", unique=True)
    pic = models.ImageField(upload_to='e_img', verbose_name="头像图片")
    # password = models.CharField(max_length=50, verbose_name='密码')
    email = models.CharField(max_length=50, verbose_name='邮箱')
    o_contact = models.CharField(max_length=20, verbose_name='其他联系方式')
    service = models.CharField(max_length=10, verbose_name='所需服务', blank=True)
    position = models.CharField(max_length=10, verbose_name='职位', blank=True)
    products = models.CharField(max_length=20, verbose_name='公司产品', blank=True)
    address = models.CharField(max_length=20, verbose_name="公司地址")
    grade = models.IntegerField(verbose_name="等级", default=0)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=2, verbose_name='用户状态审核')
    user_id = models.OneToOneField(to="User", to_field="type_id", default=2, unique=True, verbose_name='用户身份')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创新时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='审核时间')

    class Meta:
        db_table = 'ep_users'
        verbose_name = '企业信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.e_name
