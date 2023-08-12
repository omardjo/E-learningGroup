
from django.urls import path
from . import views
urlpatterns = [
    path('modules/',views.list_modules, name='module-list'),
    path('modules/<int:pk>/', views.get_module, name='module-detail'),
    path('modules/<int:pk>/update/', views.update_module, name='module-update'),
    path('modules/<int:pk>/delete/', views.delete_module, name='module-delete'),
    path('modules/create/', views.create_module, name='module-create'),
]
