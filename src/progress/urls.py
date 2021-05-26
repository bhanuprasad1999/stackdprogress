from django.urls import path
from . import views

urlpatterns = [
    path('<str:userid>/Progress/',views.progress,name='progress'),
    path('daysheet/',views.daysheet,name='daysheet'),
    path('pagenotfound/',views.pagenotfound,name='pagenotfound'),
]