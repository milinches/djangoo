from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.HomePage.as_view(), name="list"),
    path('track-nil/', views.ListPageN.as_view(), name="list_page"),
    path('track-del/', views.ListPageD.as_view(), name="list_del"),
    path('track-otw/', views.ListPageO.as_view(), name="list_otw"),
    path('<slug:slug>/', views.DetailPage.as_view(), name="detail"),
]
