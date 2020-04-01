from django.db import models

class User(models.Model):  # 建立创建表的类
    SEX = (
        ('0', '男'),
        ('1', '女'),
    )
    name = models.CharField(max_length=20,
                            help_text="用户名")
    password = models.CharField(max_length=32, help_text="密码")
    sex = models.IntegerField(choices=SEX, null=True, blank=True)  # 数据库存0,1，展示男女

    def __str__(self):  # 当对象以字符串返回时。把name返回
        return self.name