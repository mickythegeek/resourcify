from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_single/<str:pk>', views.post_single, name='post_single')
]