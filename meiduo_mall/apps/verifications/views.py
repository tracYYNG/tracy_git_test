from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from libs.captcha.captcha import captcha
from django_redis import get_redis_connection

# Create your views here.
class ImageCodeView(View):

    def get(self,request,uuid):
        #1.获取uuid
        #2.获取文本和图片二进制
        text,image = captcha.generate_captcha();
        #3.将文本和uuid存入redis
        redis_cli = get_redis_connection('code')
        redis_cli.setex(uuid,100,text)
        #4.将图片二进制返回
        return HttpResponse(image,content_type='image/jpeg')