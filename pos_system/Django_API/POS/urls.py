# from django.urls import re_path as url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="POS")
    # url(r'^department$', views.departmentApi),
    # url(r'^department/([0-9]+)$', views.departmentApi)
]
