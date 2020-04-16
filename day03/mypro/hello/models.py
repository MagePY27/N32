from django.db import models


# Create your models here.

class User(models.Model):
    SEX = (
        (0, '男'),
        (1, '女'),
    )
    user = models.CharField(max_length=15, help_text="用户名")
    name = models.CharField(max_length=15, help_text="名字")
    password = models.CharField(max_length=32, help_text="密码")
    sex = models.IntegerField(choices=SEX, null=True, blank=True)
    age = models.IntegerField(default=0, help_text="年龄")


    def __str__(self):
        return self.name