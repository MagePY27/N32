from django.shortcuts import render
from django.http import HttpResponse, QueryDict
# from hello.models import User

#普通参数的接收方法,
# def index(request):
#     # 设置默认值的方式获取更优雅
#     year = request.GET.get("year", '2020')
#     # 直接获取数据，没有传参会报错，不建议
#     month = request.GET('month')
#     return HttpResponse("year is {}, month is {}".format(year, month))

#位置传参的接收方法
# def index(request,year,month):
#     return HttpResponse("year is %s, month is %s" %(year, month))

#关键字传参的接收方法
# def index(request, **kwargs):
#     print(kwargs)
#     year = kwargs.get('year')
#     month = kwargs.get('month')
#     return HttpResponse("year is %s, month is %s" % (year, month))



# def index(request):
#     print(request.scheme)
#     print(request.method)
#     print(request.headers)
#     print(request.path)
#     print(request.META)
#     print(request.GET)
#     data = request.GET
#     year = data.get("year", "2019")
#     month = data.get("month", "10")
#     if request.method == "POST":
#         print(request.method)
#         print(request.body)
#         print(QueryDict(request.body).dict())
#         print(request.POST)
#         data = request.POST
#         year = data.get("year", "2018")
#         month = data.get("month", "07")
#     return HttpResponse("year is %s, month is %s" % (year, month))

def index(request):
    classname = "DevOps"
    return render(request, "hello/hello.html",)

def list(request):
    messages = "abcdefageae"
    users = [
        {'username': 'kk1', 'name_cn': 'kk1', 'age': 18},
        {'username': 'kk2', "name_cn": 'kk2', 'age': 19},
        {'username': 'kk3', "name_cn": 'kk3', 'age': 20},
    ]

    print(users, messages)
    return render(request, 'hello/hello.html', {'users': users, 'messages': messages})