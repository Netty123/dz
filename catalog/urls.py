from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<slug:slug>/', views.phone_detail, name='phone_detail'),
]