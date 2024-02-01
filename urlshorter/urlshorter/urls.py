from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('adminos/', views.adminos),
    path('<str:short_url>', views.redirection)
]
