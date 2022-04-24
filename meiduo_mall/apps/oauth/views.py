
from urllib import response
from django.http import JsonResponse
from apps.oauth.models import OAuthQQUser
from meiduo_mall import settings
from django.views import View
from QQLoginTool.QQtool import OAuthQQ
from django.contrib.auth import login

# Create your views here.
class QQLoginURLView(View):
    
    def get(self,request):
        qq = OAuthQQ(
            client_id=settings.QQ_CLIENT_ID, 
            client_secret=settings.QQ_CLIENT_SECRET, 
            redirect_uri=settings.QQ_REDIRECT_URL, 
            state= 'xxxx'
        )

        url = qq.get_qq_url()
        return JsonResponse({'code':0,'login_url':url})

# code = 3D0195D33335A8CE183508F92E21AA83
class OAuthQQView(View):

    def get(self,request):
        code = request.GET.get('code')
        if code is None:
            return JsonResponse({'code':400,'errmsg':'code不存在'})

        qq = OAuthQQ(
            client_id=settings.QQ_CLIENT_ID, 
            client_secret=settings.QQ_CLIENT_SECRET, 
            redirect_uri=settings.QQ_REDIRECT_URL, 
            state= 'xxxx'
        )

        token = qq.get_access_token(code)
        openid = qq.get_open_id(token)
            
        try:
            qquser = OAuthQQUser.objects.get(openid=openid)
        except:
            return JsonResponse({'code':400,'errmsg':'未绑定账号'})
        login(request,qquser.user)

        response = JsonResponse({'code':0,'errmsg':'ok'})
        response.set_cookie('username',qquser.user.username)
        return response