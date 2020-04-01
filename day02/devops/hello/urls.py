from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('hello/', views.index, name='index')
    # re_path('([0-9]{4})/([0-9]{2})/', views.re_index, name='re_index'),
    # re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', views.re_index, name='re_index')
    path('userlist/', views.userlist, name='list'),
    path('useradd/', views.useradd, name='add'),
    re_path('useredit/([0-9]{1,4})/', views.useredit, name='useredit'),
    re_path('userdel/([0-9]{1,4})', views.userdel, name='del'),
]