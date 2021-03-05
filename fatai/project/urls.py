from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.HomePage.as_view(), name="list"),
    path('track/', views.ListPage.as_view(), name="list_page"),
    path('track/<slug:slug>/', views.DetailPage.as_view(), name="detail"),
    path('track/add', views.CreateTrack.as_view(), name="add"),
]
