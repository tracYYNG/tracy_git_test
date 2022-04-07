from operator import mod
from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.
class BookInfo(models.Model):

    name = models.CharField(max_length=20,verbose_name='Book Name')
    pub_date = models.DateField(verbose_name='Release Time',null=True)
    readcount = models.IntegerField(default=0,verbose_name='Reading Volume')
    commentcount = models.IntegerField(default=0,verbose_name='Comment Volume')
    id_delete = models.BooleanField(default=False,verbose_name='Logical Deletion')

    class Meta:
        db_table = 'bookinfo'
        verbose_name = 'book'


    def __str__(self) -> str:
        return self.name
