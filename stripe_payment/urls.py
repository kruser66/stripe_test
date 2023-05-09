from django.http import HttpResponseRedirect
from django.contrib import admin
from django.urls import path, include, reverse
from payments.views import api_item, api_buy, success, cancel

def redirect2admin(request):
    return HttpResponseRedirect(reverse('admin:index'))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect2admin),
    path('item/<pk>', api_item, name='item'),
    path('buy/<pk>', api_buy, name='buy'),
    path('success', success),
    path('cancel', cancel)    
]
