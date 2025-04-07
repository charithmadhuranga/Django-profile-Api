from django.urls import path
from profile_api import views

urlpatterns = [
    path('',views.HelloApiView.as_view()),
]