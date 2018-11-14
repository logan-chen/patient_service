from django.conf.urls import url
from . import views

urlpatterns = [

    # /verifications/smscodes/(?P<mobile>1[345789]\d{9})/?
    url(r'^smscodes/(P<mobile>1[3456789]\d{9})/$',views.RegisterSmscodeView.as_view()),
]