import json
from random import randint
from django.http import HttpResponse, JsonResponse
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


class SmsCodeView(View):

    def get(self,request,mobile):
        

        # 获取参数
        image_code = request.GET.get('image_code')
        uuid = request.GET.get('image_code_id')

        # 验证参数
        if not all([image_code,uuid]):
            return JsonResponse({'code':400,'errmsg':'参数不全'})

        redis_cli = get_redis_connection('code')
        if redis_cli.get('send_flag%s'%mobile):
            return JsonResponse({'code':400,'errmsg':'请稍后发送'})

        redis_image_code = redis_cli.get(uuid)
        if redis_image_code is None:
            return JsonResponse({'code':400,'errmsg':'图片验证码过期'})

        if image_code.lower() != redis_image_code.decode().lower():
            return JsonResponse({'code':400,'errmsg':'图片验证码不匹配'})

        # 生成短信验证码
        sms_code = '%06d'%randint(0,999999)


        # 通过管道技术pipeline，实现一次连接发送多个指令
        pipeline = redis_cli.pipeline()
        # 保存短信验证码
        pipeline.setex(mobile,300,sms_code)

        # 避免频繁发送短信
        pipeline.setex('send_flag%s'%mobile,60,1)

        pipeline.execute()

        # 发送验证码
        return JsonResponse({'code':0,'errmsg':sms_code})
        