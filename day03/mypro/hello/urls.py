from django.urls import path, re_path
from . import views, views2, views3


app_name = "hello"

urlpatterns = [
    path('', views.index),
    # path('userlist/', views.userlist, name='userlist'),
    # path('useradd/', views.useradd, name='useradd'),
    # re_path('modify/(?P<id>[0-9]+)?/', views.modify, name='modify'),
    # re_path('userdel/(?P<id>[0-9]+)?/', views.userdel, name='userdel'),
    # path('user_list/', views.user_list, name='list'),
    # path('user_add/', views.user_add, name='add'),
    # re_path('user_edit/([0-9]{1,4})/', views.user_edit, name='useredit'),
    # re_path('user_del/([0-9]{1,4})', views.user_del, name='del'),

    # path('index/', views2.index),
    # path('index0/', views2.IndexView.as_view(), name='index0'),

    # View
    # path('index1/', views2.MyView.as_view(message="Hello"), name='index1'),
    path('index1/', views2.IndexView1.as_view(), name='index1'),

    # TemplateView
    path('index2/', views2.IndexView2.as_view(), name='index2'),

    # ListView--查询数据表所有数据
    path('index3/', views2.IndexView3.as_view(), name='index3'),
    path('userlist/', views3.UserList.as_view(), name='userlist'),

    # DetailView--查询数据表的某一条数据
    re_path('index4/(?P<pk>[0-9]+)?/', views2.IndexView4.as_view(), name="index4"),


    # CreateView——创建数据
    # path('index5/', views2.IndexView5.as_view(), name="index5"),
    path('useradd/', views3.UserCreate.as_view(), name="useradd"),

    # UpdateView——更新数据
    # re_path('index6/(?P<pk>[0-9]+)?/', views2.IndexView6.as_view(), name='index6'),
    re_path('modify/(?P<pk>[0-9]+)?/', views3.UserUpdate.as_view(), name="modify"),

    # DeleteView——删除数据
    # re_path('index7/(?P<pk>[0-9]+)?/', views2.IndexView7.as_view(), name="index7"),
    re_path('userdel/(?P<pk>[0-9]+)?/', views3.UserDelete.as_view(), name="userdel"),
]

#