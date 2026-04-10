from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('climatic-data/', views.climatic_data, name='climatic_data'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('remove-user/<int:user_id>/', views.remove_user, name='remove_user'),
]