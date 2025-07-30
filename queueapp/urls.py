from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('join/', views.join_queue, name='join'),
    path('queue-data/', views.get_queue_data, name='queue_data'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/action/<int:user_id>/<str:action>/', views.queue_action, name='queue_action'),
    path('dashboard/search/', views.search_queue, name='search_queue'),
    path('dashboard/reset/', views.reset_queue, name='reset_queue'),
    path('dashboard/close/', views.toggle_queue_status, name='toggle_queue'),
       
]
