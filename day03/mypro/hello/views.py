from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# get_object_or_404 用来返回http请求
# 格式: get_object_or_404(models, **kwargs)
from django.shortcuts import get_object_or_404
from django.http import Http404

import traceback
# Create your views here.


def index(request):
    return HttpResponse('<p>Hello World. </p>')



def useradd(request):
    """
        添加用户
        request 获取表单提交的数据有多种方式：
        1. request.POST.get--适用于获取单个变量进行处理的场景
        2. request.POST.dict()--适用于将表单所有数据整体处理的场景
        3. Form(request.POST)--适用于表单类验证的场景（生产最中常用）
    """
    msg = {}
    if request.method == "POST":
        try:
            # print(request.POST)
            data = request.POST.dict()
            # print(data)
            User.objects.create(**data)
            msg = {"code": 0, "result": "添加用户成功"}
        except Exception as e:
            msg = {"code": 1, "result": "添加失败: 此用户已存在"}
    return render(request, 'hello/useradd.html', {"msg": msg})


def userlist(request):
    """
    用户列表 && 姓名搜索
    """
    keyword = request.GET.get("keyword", "")
    print(keyword)
    users = User.objects.all()
    if keyword:
        users = users.filter(name__icontains=keyword)
    return render(request, 'hello/userlist.html', {"users": users, "keyword": keyword})


def modify(request, **kwargs):
    """
    用户更新
    1. 通过ID拿到要更新的数据，并传到前端渲染
    2. 将修改后的数据提交到后端
    :param request:
    :param kwargs:
    :return:
    """
    msg = {}
    id = kwargs.get('id')
    # print(id)
    user = get_object_or_404(User, id=id)
    # print(user)
    if request.method == "POST":
        try:
            data = request.POST.dict()
            #print(data)
            #User.objects.filter(id=id).update(**data)
            user.update(**data)
            msg = {"code": 0, "result": "更新用户成功"}
        except:
            msg = {"code": 1, "errmsg": "更新用户失败：{}".format(traceback.format_exc())}

    return render(request, 'hello/modify.html', {"user": user, "msg":msg})


def userdel(request, **kwargs):
    msg = {}
    id = kwargs.get('id')
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        print('404')
        raise Http404
    if request.method == "POST":
        try:
            user.delete()
            print('删除用户')
            # User.objects.get(id=id).delete()
            msg = {"code": 0, "result": "删除用户成功"}
        except:
            msg = {"code": 1, "errmsg": "删除用户失败: {}".format(traceback.format_exc())}
    return render(request, 'hello/userdel.html', {'user': user, "msg":msg})
