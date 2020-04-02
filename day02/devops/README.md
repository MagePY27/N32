### 用户管理系统

##### 用户管理系统模型

```
from django.db import models

# Create your models here.
class User(models.Model):
    SEX = (
        (0, '男'),
        (1, '女'),
    )
    user = models.CharField(max_length=20, unique=True, help_text="用户名")
    name = models.CharField(max_length=10, help_text="姓名")
    password = models.CharField(max_length=32, help_text="密码")
    age = models.IntegerField(default=0)
    sex = models.IntegerField(choices=SEX, null=True, blank=True)


    def __str__(self):
        return self.name

```

##### 配置路由 urls

```
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_list/', views.user_list, name='list'),
    path('user_add/', views.user_add, name='add'),
    re_path('user_edit/([0-9]{1,4})/', views.user_edit, name='useredit'),
    re_path('user_del/([0-9]{1,4})', views.user_del, name='del'),
]
```

##### 配置视图 views

```
from django.shortcuts import render, redirect
from django.http import HttpResponse, QueryDict, HttpResponseRedirect
from hello.models import User


#所有用户列表
def user_list(request):
    users = User.objects.all()
    return render(request, 'hello/index.html', {'users': users})


#添加用户
def user_add(request):
    u = User.objects
    try:
        if request.method == 'POST':
            # print(QueryDict(request.body).dict())
            data = QueryDict(request.body).dict()
            u.get_or_create(**data)
    except:
        return HttpResponse('此用户已存在')

    return render(request,'hello/useradd.html')


#编辑用户信息
def user_edit(request, u_id):
    u = User.objects.get(id=u_id)
    # print(u.user, u.name, u.age)

    if request.method == "POST":
        u = User.objects.filter(id=u_id)
        print(QueryDict(request.body).dict())
        data = QueryDict(request.body).dict()
        u.update(**data)

    return render(request, 'hello/useredit.html', {"user": u})
    

#删除用户
def user_del(request, u_id):
    u = User.objects.get(id=u_id)

    if request.POST.get('delete') == "True":
        print(request.POST.get('delete'))
        u.delete()
        return render(request, 'hello/index.html', {"users": User.objects.all()})

    return render(request, 'hello/userdel.html', {"user": u})
```

创建模板 userlist.html、useradd.html、useredit.html、userdel.html

```
cat  hello/templates/index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>用户管理系统</title>
</head>
<body>
<b><a href="/hello/user_add/">添加用户</a></b>
<table border="1">
    <tr>
        <th>ID</th>
        <th>用户名</th>
        <th>姓名</th>
        <th>年龄</th>
        <th>性别</th>
        <th>操作</th>
    </tr>
    {% for u in users %}
    <tr>
        <td>{{u.id}}</td>
        <td>{{u.user}}</td>
        <td>{{u.name}}</td>
        <td>{{u.age}}</td>
        <td>{{u.get_sex_display}}</td>
        <td>
            <a href="/hello/user_edit/{{u.id}}">{{ "编辑" }}</a>|
            <a href="/hello/user_del/{{u.id}}">{{"删除"}}</a>
        </td>
    </tr>
    {% endfor %}
</table>
</body>
</html>
```

