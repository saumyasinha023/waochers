"""waochers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from registration import views
from django.conf.urls import handler404,handler500

handler404 = views.error404
handler505 = views.error500

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^registration/&customer_id=(?P<id>\d+)&name=(?P<name>\w+)&email=(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})&phone=(?P<phone>\w+)&password=(?P<password>\w+)/$', views.registerCustomer),
	url(r'^login/&email=(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})&password=(?P<password>\w+)/$', views.loginEmail),
	url(r'^login/&phone=(?P<phone>\w+)&password=(?P<password>\w+)/$', views.loginPhone),
	url(r'^login/&id=(?P<id>\d+)$',views.loginFBOrGPlus),
	url(r'^forgotPassword/&email=(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})&password=(?P<password>\w+)/$', views.forgotPasswordEmail),
	url(r'^forgotPassword/&phone=(?P<phone>\w+)&password=(?P<password>\w+)/$', views.forgotPasswordPhone),
]

