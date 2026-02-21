from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('notifications/', views.NotificationsView.as_view(), name='notifications'),
    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('viewer/<uuid:id>/', views.DocumentView.as_view(), name='viewer'),
    path('documents/<str:d_type>/', views.DocumentsView.as_view(), name='documents')
]