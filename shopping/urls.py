from django.urls import path

from . import views

app_name = 'shopping'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.product_details, name='product_details'),
    path('<int:product_id>/change_category/', views.change_category, name='change_category'),
]