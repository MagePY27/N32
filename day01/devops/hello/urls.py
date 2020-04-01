from django.urls import path
from . import views
# app_name = 'hello'

urlpatterns = [
    # 普通传参方法
    path('', views.index, name='index'),

    # 位置传参
    # re_path('([0-9]{4})/([0-9]{2})/', views.index, name='index'),

    # 关键字传参
    # re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', views.index, name='index'),
    path('list/', views.list, name='list')
]