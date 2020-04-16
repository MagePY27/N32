from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.views.generic import View



def index(request):
    if request.method == 'GET':
        return HttpResponse('get')
    elif request.method == 'POST':
        return HttpResponse('post')
    elif request.method == 'PUT':
        return HttpResponse('put')
    elif request.method == 'DELETE':
        return HttpResponse('delete')


# class IndexView(View):
#     def get(self, request):
#         return HttpResponse("get")
#
#     def post(self, request):
#         return HttpResponse("post")
#
#     def put(self, request):
#         return HttpResponse("put")
#
#     def delete(self, request):
#         return HttpResponse("delete")

class IndexView(View):
    message = "Hello Django"

    def get(self, request):
        return HttpRespnse(self.message)

class MyView(IndexView):
    message = "Hello World"

    def get(self, request):
        return HttpResponse(self.message)

class IndexView1(View):
    def get(self, request):
        users = User.objects.all()
        print("index1 get")
        return render(request, 'index.html', {"users": users})

    def post(self, request):
        data = request.POST.dict()
        print(data)
        User.objects.create(**data)
        users = User.objects.all()
        return render(request, 'index.html', {"users": users})


from django.views.generic import TemplateView


class IndexView2(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView2, self).get_context_data(**kwargs)
        print(kwargs)
        # print(context, type(context))
        context['users'] = User.objects.all()
        print(context)
        return context


from django.views.generic import ListView
from django.shortcuts import render, reverse, redirect


class IndexView3(ListView):
    """
    listView适合以下场景
    getlist: 列出所有数据
    create: 创建数据
    """

    template_name = "index.html"  # 指定模板文件
    model = User  # object_list = User.objects.all()
    context_object_name = "users"  # 自定义传给前端模板渲染的变量，默认object_list
    keyword = ''

    def get_queryset(self):
        queryset = super(IndexView3, self).get_queryset()
        # print(queryset)
        self.keyword = self.request.GET.get("keyword", "")
        if self.keyword:
            queryset = queryset.filter(name__icontains=self.keyword)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        # 继承基础的ListView类
        context = super(IndexView3, self).get_context_data(**kwargs)
        # 在父类的基础上，再额外加一下数据到object_list中
        context['keyword'] = self.keyword
        print(context)
        return context


from django.views.generic import DetailView
from datetime import datetime, timezone


class IndexView4(DetailView):
    """
        获取某条记录的ID，适用于以下三种场景，核心就是拿到URL中的ID
        getone: 获取当前记录的数据
        update: 更新当前记录的数据
        delete: 删除当前记录的数据
    """

    template_name = "index.html"   #指定模板文件  ，默认detail.html
    model = User        # object = User.objects.get(pk=pk)
    print(model)
    # context_object_name = "aaa"  #定义存储返回结果的对象名，默认object

    # 在get_context_data() 函数中可以用于传递一些额外的内容到网页
    def get_context_data(self, **kwargs):
        context = super(IndexView4, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context


from django.views.generic import CreateView, UpdateView, DeleteView


class IndexView5(CreateView):
    """
    添加用户
    """
    template_name = "index.html"  #指定模板文件
    model = User
    fields = ('user','name', 'password', 'sex','age')

    def get_success_url(self):
        return reverse('hello:index5')

    def get_context_data(self, **kwargs):
        context = super(IndexView5, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context


class IndexView6(UpdateView):
    """
    更新用户
    """
    template_name = "index.html"
    model = User
    fields = ('user','name', 'password', 'sex','age')

    def get_success_url(self):
        print(self.kwargs)
        return reverse("hello:index6", kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super(IndexView6, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context


class IndexView7(DeleteView):
    """
    删除用户
    """
    template_name = "index.html"
    model = User

    def get_success_url(self):
        return reverse('hello:index3')
    #
    def get_context_data(self, **kwargs):
        context = super(IndexView7, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        print(context)
        return context