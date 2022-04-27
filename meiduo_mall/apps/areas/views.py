from django.http import JsonResponse
from django.views import View

from apps.areas.models import Areas
from django.core.cache import cache

# Create your views here.
class AddressView(View):

    def get(self,request):

        province_list = cache.get('province')
        if province_list is None:
            provinces = Areas.objects.filter(parent_id=0)

            province_list = []
            for province in provinces:
                province_list.append({
                    'id':province.id,
                    'name':province.name
                })
            
            cache.set('province',province_list,24*3600)
        
        return JsonResponse({'code':0,'errmsg':'ok','province_list':province_list})

class CityView(View):

    def get(self,request,hlevel_id):

        city_list = cache.get('city:%s'%hlevel_id)
        if city_list is None:
            citys = Areas.objects.filter(parent_id = hlevel_id)

            city_list = []
            for city in citys:
                city_list.append({
                    'id':city.id,
                    'name':city.name
                })

            cache.set('city:%s'%hlevel_id,city_list,24*3600)

        return JsonResponse({'code':0,'errmsg':'ok','city_list':city_list})
