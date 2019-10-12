from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-task/', views.get_input_text, name='add'),
    path('del-task/', views.delet_item, name='del'),
    path('ajax_send/', views.creat_ajax)
]