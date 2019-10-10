from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-task/', views.get_input_text, name='add')
]