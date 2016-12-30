"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from mysite.views import *

urlpatterns = [
    url(r'^jove/', admin.site.urls),
    url(r'^footer.html$',footer), 
    url(r'^header.html$',header), 
    url(r'^index.html$', index),
    url(r'^leftlist.html$',leftlist), 
    url(r'^other-header.html$',oheader), 
    url(r'^tool-nmap.html$', namp),
    url(r'^web-finger.html$', finger),
    url(r'^domain-info.html$',domain), 
    url(r'^common-exp.html$',exp), 
    url(r'^second-domain.html$', sdomain),
    url(r'^web-dirs.html$', dirs),
    url(r'^tool-sqlmap.html$',sqlmap), 
    url(r'^api-md5.html$',md5), 
    url(r'^tool-hydra.html$', hydra),
]
