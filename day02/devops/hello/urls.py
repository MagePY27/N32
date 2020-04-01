from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('hello/', views.index, name='index')
    # re_path('([0-9]{4})/([0-9]{2})/', views.re_index, name='re_index'),
    # re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', views.re_index, name='re_index')
    path('user_list/', views.user_list, name='list'),
    path('user_add/', views.user_add, name='add'),
    re_path('user_edit/([0-9]{1,4})/', views.user_edit, name='useredit'),
    re_path('user_del/([0-9]{1,4})', views.user_del, name='del'),
]