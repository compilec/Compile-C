"""mini URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from compilec.views import *
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from compilec import views as compilec_views

admin.autodiscover()

urlpatterns = (
   url(r'^$', index, name ='index'),
   url(r'^home/', home, name ='home'),
   url(r'^about/', about, name ='about'),
   url(r'^acc/', acc, name ='acc'),
   url(r'^logout/', logout, name ='logout'),
   url(r'^contact/',contact, name ='contact'),
   url(r'^compiler/',compiler, name ='compiler'),
   url(r'^programs/',programs, name ='programs'),
   url(r'^signup/', compilec_views.signup, name='signup'),
   url(r'^user/', include('django.contrib.auth.urls')),
   url(r'^i1/',i1, name ='i1'),
   url(r'^i2/',i2, name ='i2'),
   url(r'^i3/',i3, name ='i3'),
   url(r'^i4/',i4, name ='i4'),
   url(r'^i5/',i5, name ='i5'),
   url(r'^i6/',i6, name ='i6'),
   url(r'^ii1/',ii1, name ='ii1'),
   url(r'^iii1/',iii1, name ='iii1'),
   url(r'^iii2/',iii2, name ='iii2'),
   url(r'^iii3/',iii3, name ='iii3'),
   url(r'^iii4/',iii4, name ='iii4'),
   url(r'^iii5/',iii5, name ='iii5'),
   url(r'^iii6/',iii6, name ='iii6'),
   url(r'^iii7/',iii7, name ='iii7'),
   url(r'^iv1/',iv1, name ='iv1'),

)
