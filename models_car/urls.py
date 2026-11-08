from django.urls import path

from . import views


urlpatterns = [
    path('modelcar/list/', views.ModelCarListView.as_view(), name='modelcar_list'),
    path('modelcar/create/', views.ModelCarCreateView.as_view(), name='modelcar_create'),
    path('modelcar/update/<int:pk>/', views.ModelCarUpdateView.as_view(), name='modelcar_update'),
    path('modelcar/detail/<int:pk>/', views.ModelCarDetailView.as_view(), name='modelcar_detail'),
    path('modelcar/delete/<int:pk>/', views.ModelCarDeleteView.as_view(), name='modelcar_delete'),
]