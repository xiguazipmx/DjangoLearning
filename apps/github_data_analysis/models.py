#coding: utf-8
from django.db import models

# Create your models here.
class UserMessage(models.Model):
    user_id = models.CharField(primary_key=True, max_length=24,default="", verbose_name="主键")
    name = models.CharField(max_length=20, verbose_name=u"用户名")
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100, verbose_name=u"联系地址")
    message = models.CharField(max_length=500, verbose_name=u"留言信息")

    class Meta:
        verbose_name = u"用户留言信息"

    def __str__(self):
        return self.user_id