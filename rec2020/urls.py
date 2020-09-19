"""rec2020 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.views.static import serve
from . import views
urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('rec/', views.recResuts, name='rec'),
    path('data/', include(('dataStatistics.urls', 'dataStatistics'), namespace='data')),
    path('aiA/', include(('aiA.urls', 'aiA'), namespace='aiA')), #namespace用于在html中标识url
    path('aiB/', include(('aiB.urls', 'aiB'), namespace='aiB')),
    path('aiC/', include(('aiC.urls', 'aiC'), namespace='aiC')),
    path('kgA/', include(('kgA.urls', 'kgA'), namespace='kgA')),
    path('kgB/', include(('kgB.urls', 'kgB'), namespace='kgB')),
    path('kgInference/', include(('kgInference.urls', 'kgInference'), namespace='kgInference')),
    path('ormDesign/', include(('ormDesign.urls', 'ormDesign'), namespace='ormDesign')),
]
