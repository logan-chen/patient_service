"""patient_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from dashing.utils import router
from utils.widgets import CustomWidget
router.register(CustomWidget, 'custom_widget')

from django.contrib import admin
# from rest_framework.documentation import include_docs_urls
import xadmin
urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^dashboard/',include(router.urls)),
    url(r'^verifications', include('verifications.urls'))

    # url(r'^admin/', admin.site.urls),
    # url(r'^users/', include('user.urls')),
    # url(r'^oauth/', include('oauth.urls')),
    # url(r'^areas/', include('areas.urls')),
    # url(r'^goods/', include('goods.urls')),
    # url(r'^cart/', include('carts.urls')),
    # url(r'^orders/', include('order.urls')),
    # url(r'^pay/', include('pay.urls')),
]
