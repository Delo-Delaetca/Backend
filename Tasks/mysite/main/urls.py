from django.urls import path

from . import views

urlpatterns = [
    path('main/<str:model_name>/<int:object_id>/', views.get_model_by_id, name='get_model_by_id'),
]
