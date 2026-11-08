from django.urls import path

from . import views


urlpatterns = [
    path('brand/list/', views.BrandListView.as_view(), name='brand_list'),
    path('brand/create/', views.BrandCreateView.as_view(), name='brand_create'),
    path('brand/update/<int:pk>/', views.BrandUpdateView.as_view(), name='brand_update'),
    path('brand/detail/<int:pk>/', views.BrandDetailView.as_view(), name='brand_detail'),
    path('brand/delete/<int:pk>/', views.BrandDeleteView.as_view(), name='brand_delete'),
]