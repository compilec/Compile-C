"""mini URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  re_path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  re_path(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  re_path(r'^blog/', include('blog.urls'))
"""
from django.urls import include, re_path
from django.contrib import admin
from compilec.views import *
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from compilec import views as compilec_views

admin.autodiscover()

urlpatterns = (
   re_path(r'^$', index, name ='index'),
   re_path(r'^home/', home, name ='home'),
   re_path(r'^about/', about, name ='about'),
   re_path(r'^acc/', acc, name ='acc'),
   re_path(r'^logout/', logout, name ='logout'),
   re_path(r'^contact/',contact, name ='contact'),
   re_path(r'^compiler/',compiler, name ='compiler'),
   re_path(r'^programs/',programs, name ='programs'),
   re_path(r'^signup/', compilec_views.signup, name='signup'),
   re_path(r'^user/', include('django.contrib.auth.urls')),
   re_path(r'^i1/',i1, name ='i1'),
   re_path(r'^i2/',i2, name ='i2'),
   re_path(r'^i3/',i3, name ='i3'),
   re_path(r'^i4/',i4, name ='i4'),
   re_path(r'^i5/',i5, name ='i5'),
   re_path(r'^i6/',i6, name ='i6'),
   re_path(r'^ii1/',ii1, name ='ii1'),
   re_path(r'^iii1/',iii1, name ='iii1'),
   re_path(r'^iii2/',iii2, name ='iii2'),
   re_path(r'^iii3/',iii3, name ='iii3'),
   re_path(r'^iii4/',iii4, name ='iii4'),
   re_path(r'^iii5/',iii5, name ='iii5'),
   re_path(r'^iii6/',iii6, name ='iii6'),
   re_path(r'^iii7/',iii7, name ='iii7'),
   re_path(r'^iv1/',iv1, name ='iv1'),

)
