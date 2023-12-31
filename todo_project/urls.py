from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base, name='base'),
    path('', include('todo_app.urls')),
]
