### 用户管理系统

#### 用户管理系统模型

```python
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

#### 配置路由 urls

```python
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

#### 配置视图 views

```python
from django.shortcuts import render, redirect
from django.http import HttpResponse, QueryDict, HttpResponseRedirect
from hello.models import User


#所有用户列表
def user_list(request):
    users = User.objects.all()
    return render(request, 'hello/userlist.html', {'users': users})


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
	return redirect("/hello/user_list/")	#修改完后返回用户列表界面
      
    return render(request, 'hello/useredit.html', {"user": u})
    

#删除用户
def user_del(request, u_id):
    u = User.objects.get(id=u_id)

    if request.POST.get('delete') == "True":
        print(request.POST.get('delete'))
        u.delete()
        return redirect("/hello/user_list/")  #删除后返回用户列表界面

    return render(request, 'hello/userdel.html', {"user": u})
```

#### 创建模板 

> userlist.html

```html
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

> useradd.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>user add</title>
</head>
<body>
<b><a href="/hello/user_list/"><<返回用户界面</a></b>
<form  method="post">
用户：<input type="text" name="user" /><br />
密码：<input type="password" name="password" minlength="6"/><br />
姓名：<input type="text" name="name" /><br />
年龄：<input type="number" name="age" min="0"/><br />
性别：<input type="radio" name="sex" value="0">男 <input type="radio" name="sex" value="1">女<br />
<input type="submit" value="Submit">
<!--<a href="{{name}}" class="a_post">提交</a>-->
</form>
</body>
</html>
```

> useredit.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>user edit</title>
</head>
<body>
<!--<p>用户编辑</p>-->
<b><a href="/hello/user_list/"><<返回用户界面</a></b>
<form  method="post">
用户：<input type="text" name="user" value="{{user.user}}" /><br />
密码：<input type="password" name="password" minlength="6" value="{{user.password}} "/><br />
姓名：<input type="text" name="name" value="{{user.name}} "/><br />
年龄：<input type="number" name="age" min="0" value="{{user.age}}" /><br />
性别：<input type="radio" name="sex" value="0">男 <input type="radio" name="sex" value="1">女<br />
<input type="submit" value="Submit">
</form>
</body>
</html>
```

> userdel.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>user delete</title>
</head>
<body>
<b><a href="/hello/user_list/"><<返回用户界面</a></b>
<form  method="post">
    <b>删除用户{{user.user}}?</b><br>
<!--    <a href="/hello/userdel/{{user.id}}/delete=True">Yes</a>/<a href="/hello/userlist/">No</a>-->
    <input type="radio" name="delete" value=True>是<input type="radio" name="delete" value=False>否
    <input type="submit" value="Submit">
</form>
</body>
</html>
```

### 展示效果

#### 用户列表

![image-20200402112854120](https://github.com/MagePY27/P27N32-SunHao/blob/master/day02/devops/static/img/image-20200402112854120.png ) 

#### 添加用户

> 点击添加用户

![image-20200402113006952](https://github.com/MagePY27/P27N32-SunHao/blob/master/day02/devops/static/img/image-20200402113006952.png)	

> 填写用户信息

![image-20200402113421423](https://github.com/MagePY27/P27N32-SunHao/blob/master/day02/devops/static/img/image-20200402113421423.png)	

> 提交信息，返回用户界面可以看到新添加的用户

![image-20200402113455397](https://github.com/MagePY27/P27N32-SunHao/blob/master/day02/devops/static/img/image-20200402113455397.png)		

#### 编辑用户

> 点击编辑

![image-20200402113558206](https://github.com/MagePY27/P27N32-SunHao/blob/master/day02/devops/static/img/image-20200402113558206.png)	

> 修改年龄为33岁，并将性别改为女	

![image-20200402113643671](https://github.com/MagePY27/P27N32-SunHao/blob/master/day02/devops/static/img/image-20200402113643671.png)	

> 提交修改，返回用户列表，看到修改结果	

![image-20200402113717322](https://github.com/MagePY27/P27N32-SunHao/blob/master/day02/devops/static/img/image-20200402113717322.png)		

#### 删除用户

> 点击删除

![image-20200402114324096](https://github.com/MagePY27/P27N32-SunHao/blob/master/day02/devops/static/img/image-20200402114324096.png)	

> 删除确认，点击是并提交

![image-20200402114545284](https://github.com/MagePY27/P27N32-SunHao/blob/master/day02/devops/static/img/image-20200402114545284.png)	

> 此时看到用户界面此用户已被删除

![image-20200402115044673](https://github.com/MagePY27/P27N32-SunHao/blob/master/day02/devops/static/img/image-20200402115044673.png)		

