from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.HomePage.as_view(), name="list"),
    path('track/', views.)
]
