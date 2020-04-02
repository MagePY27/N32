from django.shortcuts import render, redirect
from django.http import HttpResponse, QueryDict, HttpResponseRedirect
from hello.models import User
import datetime


def user_list(request):
    users = User.objects.all()
    return render(request, 'hello/userlist.html', {'users': users})


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


def user_edit(request, u_id):
    u = User.objects.get(id=u_id)
    # print(u.user, u.name, u.age)

    if request.method == "POST":
        u = User.objects.filter(id=u_id)
        print(QueryDict(request.body).dict())
        data = QueryDict(request.body).dict()
        u.update(**data)
        return redirect("/hello/user_list/")

    return render(request, 'hello/useredit.html', {"user": u})


def user_del(request, u_id):
    u = User.objects.get(id=u_id)

    if request.POST.get('delete') == "True":
        print(request.POST.get('delete'))
        u.delete()
        # return HttpResponse("delete user {}".format(u))
        return redirect("/hello/user_list/")

    return render(request, 'hello/userdel.html', {"user": u})


# def index(request):
    # return HttpResponse("<p>Hello World, Hello, Django</p>")

# def re_index(request, year, month):
#     #year = request.GET.get("year", "2019")
#     #month = request.GET["month"]
#     # year = kwargs.get('year')
#     # month = kwargs.get('month')
#     return HttpResponse("year is {}, month is {}".format(year, month))

# def index_post(request):
#     #print(request.scheme)
#     # print(request.method)
#     # print(request.headers)
#     # print(request.path)
#     # print(request.META)
#     # print(request.GET)
#     data = request.GET
#     year = data.get('year', '2020')
#     month = data.get('month', '01')
#     if request.method == "POST":
#         # print(request.method)
#         print(request.body)
#         # print(request.POST)
#         # print(QueryDict(request.body).dict())
#         #data = request.POST
#         year = request.POST.get('year', '2018')
#         month = request.POST.get('month', '03')
#
#     # return HttpResponse('Year is {}, month is {}'.format(year, month))
#     return HttpResponse("year is %s, month is %s" % (year, month))


# def index(request):
#     classname = "DevOps"
#     books = ['Python', 'Java', 'Django']
#     user = {'name':'kk', 'age':18}
#     userlist = [{'name':'kk','age':18},{'name':'rock', 'age':19},{'name':'mage', 'age':20}]
#     messages = "ab"
#     val = [2018,'abc','ww22']
#     value = datetime.datetime.now()
#     return render(request, 'hello/hello.html', {'classname': classname, "books": books, "user": user, "userlist": userlist,
#                                                 "messages": messages, "val":val, "value": value})

