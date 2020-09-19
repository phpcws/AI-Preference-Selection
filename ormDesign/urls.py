from django.urls import path
from . import views
urlpatterns = [
    path('', views.getCategory, name='category'),
    path('1', views.getProvinces, name='province'),
    path('1/2', views.getFirstLevel, name='firstlevel'),
    path('1/2/3', views.getColleges, name='college'),
    path('1/2/3/4', views.getMajors, name='major'),
    path('1/2/3/4/5',views.getRankings,name='ranking'),
]