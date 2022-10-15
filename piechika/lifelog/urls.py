from django.urls import path
from . import views

urlpatterns = [
    path('', views.sleeplogListView.as_view(), name='index'),
    path('sleeplog/create/', views.sleeplogCreateView.as_view(), name='create'),
    path('sleeplog/detail/<int:pk>', views.sleeplogDetailView.as_view(), name='detail'),
    path('sleeplog/update/<int:pk>', views.sleeplogUpdateView.as_view(), name='update'),
    path('sleeplog/delete/<int:pk>', views.sleeplogDeleteView.as_view(), name='delete'),
]