from django.urls import path
from . import views

urlpatterns = [
    # path('', views.item, name='catalog'),
    path('items/', views.item, name='catalog'),
    path('items/<int:item_id>/', views.item_details, name='item-details'),
    path('items/add/', views.add_item, name='add-item'),
    path('items/change/<int:item_id>/', views.change_item, name='change-item'),
    path('items/delete/<int:item_id>/', views.delete_item, name='delete-item'),
]
