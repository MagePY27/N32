from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from django.views.generic import View
from django.shortcuts import render, reverse, redirect
from django.contrib.messages.views import SuccessMessageMixin


class UserList(ListView):
    template_name = 'hello/userlist.html'
    model = User
    # context_object_name = "users"

    keyword = ''

    def get_queryset(self):
        queryset = super(UserList, self).get_queryset()
        # print(queryset)
        self.keyword = self.request.GET.get("keyword", "")
        # print(self.keyword)
        if self.keyword:
            queryset = queryset.filter(user__icontains=self.keyword)
            print(queryset)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        # 继承基础的ListView类
        context = super(UserList, self).get_context_data(**kwargs)
        # 在父类的基础上，再额外加一下数据到object_list中
        context['keyword'] = self.keyword
        return context


class UserCreate(SuccessMessageMixin, CreateView):
    """
    添加用户
    """
    template_name_suffix = 'add'  # 修改模板后缀为add， useradd
    # template_name = "hello/useradd.html"  #指定模板文件
    model = User
    fields = ('user','name', 'password', 'sex','age')
    success_message = "%(name)s was create successfully"
    # msg = ""


    def get_success_url(self):
        print(self.request.POST)
        if '_addanother' in self.request.POST:
            return reverse('hello:useradd')
        return reverse('hello:userlist')

    # def get_context_data(self, **kwargs):
    #     # print(kwargs)
    #     context = super(UserCreate, self).get_context_data(**kwargs)
    #     # aaa = self.get_success_message(form.cleaned_data)
    #     # context['msg'] = {"code": 0, "result": "添加用户成功"}
    #     # print(context)
    #     return context

    # def form_valid(self, form):
    #     """
    #     如果 表单有效，则重定向到所提供的url
    #     """
    #     print(form)
    #     # return self.render_to_response(response=response)
    #     return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        # print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))


class UserUpdate(SuccessMessageMixin, UpdateView):
    """
    更新用户
    """
    template_name = "hello/modify.html"
    model = User
    fields = ('user', 'name', 'password', 'sex', 'age')
    # context_object_name = "user"
    # success_message = "%(name)s was update successfully"
    success_message = "%(user)s was create successfully"


    def get_success_url(self):
        # print(self.kwargs)
        print(self.request.POST)
        if '_continue' in self.request.POST:
            return reverse('hello:modify', kwargs={'pk': self.object.pk})
        # return reverse("hello:modify", kwargs={'pk': self.kwargs['pk']})
        return reverse('hello:userlist')


class UserDelete(DeleteView):
    """
    删除用户
    """
    template_name = "hello/userdel.html"
    model = User

    def get_success_url(self):
        return reverse('hello:userlist')
