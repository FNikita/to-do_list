from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='index'),
    path('ajax-req/', views.ajax_task, name='ajax_req'),
]