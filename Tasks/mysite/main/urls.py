from django.urls import path
from . import views
from .models import User

urlpatterns = [
    path('', views.index),
    path('read/<int:id>', views.read),
    path('create', views.create),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
]