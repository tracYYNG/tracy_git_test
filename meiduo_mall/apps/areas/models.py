from operator import mod
from tabnanny import verbose
from django.db import models

# Create your models here.
class Areas(models.Model):
    code=models.CharField(unique=True,max_length=12,verbose_name='编号')
    name=models.CharField(max_length=20,verbose_name='名称')
    parent=models.ForeignKey('self',on_delete=models.SET_NULL,
                            related_name='subs',null=True,default=0,
                            blank=True,verbose_name='上级行政区')

    class Meta:
        db_table = 'tb_areas'
        verbose_name = '省市区'
        verbose_name_plural = verbose_name