from django.urls import path
from . import views

urlpatterns = [
    path('', views.sleeplogListView.as_view(), name='index'),
    path('sleeplog/detail/<int:pk>', views.sleeplogDetailView.as_view(), name='detail'),
]