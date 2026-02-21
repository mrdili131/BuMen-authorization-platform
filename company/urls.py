from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('',views.IndexView.as_view(),name='home'),
    path('create_request/',views.CreateRequest.as_view(),name='create_request')
]