import json
import re
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from apps.user.models import User

from django.contrib.auth import login

# Create your views here.

# 验证用户名是否存在
"""
请求：接收用户名
业务逻辑：根据用户名查询数据库
响应：JSON
{code:状态码（成功为0）, count:0/1, errmsg: ok}
"""
class UsernameCountView(View):
    
    def get(self,requset,username):
        count = User.objects.filter(username=username).count()
        return JsonResponse({'code':0,'count':count,'errmsg':'ok'})

class MobileCountView(View):

    def get(self,request,mobiles):
        count = User.objects.filter(mobiles=mobiles).count()
        return JsonResponse({'code':0,'count':count,'errmsg':'ok'})

class RegisterView(View):

    def post(self,request):
        body_base = request.body
        body_str = body_base.decode()
        body_json = json.loads(body_str)

# username: this.username,
# password: this.password,
# password2: this.password2,
# mobile: this.mobile,
# allow: this.allow.toString()

        username=body_json.get('username')
        password=body_json.get('password')
        password2=body_json.get('password2')
        mobile=body_json.get('mobile')
        allow=body_json.get('allow')

        if not all([username,password,password2,mobile,allow]):
            return JsonResponse({'code':400,'errmsg':'参数不全'})

        if not re.match('[0-9A-Za-z]{5,20}',username):
            return JsonResponse({'code':400,'errmsg':'用户名不符合规则'})

        if not re.match('[0-9A-Za-z]{5,20}',password):
            return JsonResponse({'code':400,'errmsg':'密码不符合规则'})

        if password2 != password:
            return JsonResponse({'code':400,'errmsg':'确认密码与密码不同'})

        if not re.match('(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}',mobile):
            return JsonResponse({'code':400,'errmsg':'手机号码不符合规则'})

        if allow == 0:
            return JsonResponse({'code':400,'errmsg':'没有同意使用协议'})

        

        user = User.objects.create_user(username=username,password=password,mobiles=mobile)
        login(request,user)

        return JsonResponse({'code':0,'errmsg':'ok'})
