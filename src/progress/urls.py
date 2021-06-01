from django.urls import path
from . import views

urlpatterns = [
    path('<str:userid>/Progress/<int:day>',views.progress,name='progress'),
]