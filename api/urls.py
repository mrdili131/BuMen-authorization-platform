from django.urls import path
from . import views


urlpatterns = [
    path('reject/',views.DocumentRejectAPI.as_view()),
    path('sign/',views.DocumentSignAPI.as_view())
]