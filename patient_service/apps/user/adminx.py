import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from .models import User, Patient, Doctor, Enterprise


class BaseSetting:
    enable_themes = True
    use_bootswatch = True


class GlobalSetting:
    site_title = '全国患者服务中心后台管理'
    site_footer = '上海皓推信息科技有限公司'
    menu_style = 'accordion'


xadmin.site.register(views.base.BaseAdminView, BaseSetting)
xadmin.site.register(xadmin.views.base.CommAdminView, GlobalSetting)


class PatientAdmin(object):
    # 选择显示的字段
    list_display = ['id', 'name', 'gender', 'phone', 'age', 'pic', 'city_info', 'height', 'weight', 'o_contact', 'disease_info', 'treatment_info', 'join', 'case_img', 'create_time', 'status', 'recommend_id']

    # 添加字段搜索,不能添加外键字段,否则会报错
    search_fields = ['phone', 'recommend_id', 'city_info', 'treatment_info', 'join']

    # 过滤器
    list_filter = ['disease_info', 'join', 'create_time', 'status', 'update_time']

    # 按照create_time降序排列，同时也可以在标题栏点击降序
    ordering = ['-create_time']

    # 自定制图标显示
    # model_icon = 'fa fa-beer'
    # css文件：xadmin/static/xadmin/vendor/font-awesome/css/font-awesome.css
    # 可以下载最新版本的，http://fontawesome.dashgame.com/，直接复制标签的类即可使用

    # 设置只读字段，在修改页面为p标签
    readonly_fields = ['phone', 'user_id']

    # 设置不显示某些字段，修改页面隐藏该字段
    # exclude = ['price']

    # 只要是涉及到此model的外键都会显示查询，不会出现下拉框，优点是当数据量过大时候，不会加载所有数据
    # relfield_style = 'fk-ajax'

    # 设置在列表页页面可编辑的字段
    list_editable = ['join', 'status', 'recommend_id', 'create_time']


class DoctorAdmin(object):
    # 选择显示的字段
    list_display = ['id', 'name', 'gender', 'affiliated_hospital', 'department', 'phone', 'age', 'pic', 'city_info', 'nickname', 'o_contact', 'create_time', 'status', 'recommend_id']

    # 添加字段搜索,不能添加外键字段,否则会报错
    search_fields = ['phone', 'recommend_id', 'city_info', 'join', 'department', 'affiliated_hospital']

    # 过滤器
    list_filter = ['department', 'affiliated_hospital', 'city_info',  'create_time', 'status', 'update_time']

    # 按照create_time降序排列，同时也可以在标题栏点击降序
    ordering = ['-create_time']

    # 自定制图标显示
    # model_icon = 'fa fa-beer'
    # css文件：xadmin/static/xadmin/vendor/font-awesome/css/font-awesome.css
    # 可以下载最新版本的，http://fontawesome.dashgame.com/，直接复制标签的类即可使用

    # 设置只读字段，在修改页面为p标签
    readonly_fields = ['phone', 'user_id']

    # 设置不显示某些字段，修改页面隐藏该字段
    # exclude = ['price']

    # 只要是涉及到此model的外键都会显示查询，不会出现下拉框，优点是当数据量过大时候，不会加载所有数据
    # relfield_style = 'fk-ajax'

    # 设置在列表页页面可编辑的字段
    list_editable = ['join', 'status', 'recommend_id', 'update_time']


class EnterpriseAdmin(object):
    # 选择显示的字段
    list_display = ['id', 'e_name', 'name', 'phone', 'email', 'pic', 'position', 'address', 'o_contact', 'create_time', 'status', 'products', 'grade']

    # 添加字段搜索,不能添加外键字段,否则会报错
    search_fields = ['products', 'address']

    # 过滤器
    list_filter = ['status', 'create_time', 'update_time']

    # 按照students_num降序排列，同时也可以在标题栏点击降序
    ordering = ['-create_time']

    # 自定制图标显示
    # model_icon = 'fa fa-beer'
    # css文件：xadmin/static/xadmin/vendor/font-awesome/css/font-awesome.css
    # 可以下载最新版本的，http://fontawesome.dashgame.com/，直接复制标签的类即可使用

    # 设置只读字段，在修改页面为p标签
    readonly_fields = ['phone', 'user_id']

    # 设置不显示某些字段，修改页面隐藏该字段
    # exclude = ['price']

    # 只要是涉及到此model的外键都会显示查询，不会出现下拉框，优点是当数据量过大时候，不会加载所有数据
    # relfield_style = 'fk-ajax'

    # 设置在列表页页面可编辑的字段
    list_editable = ['grade', 'status', 'update_time']


xadmin.site.register(Patient, PatientAdmin)
xadmin.site.register(Doctor, DoctorAdmin)
xadmin.site.register(Enterprise, EnterpriseAdmin)