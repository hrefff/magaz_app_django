from django.urls import path
from . import views

urlpatterns = [
    path('income/', views.income, name='income'),
    path('income/add/', views.add_income, name='add-income'),
    path('income/<int:income_id>/', views.income_details, name='income-details'),
    path('sale/', views.sale, name='sale'),
    path('sale/<int:sale_id>/', views.sale_details, name='sale-details'),
    path('sale/add/', views.add_sale, name='add-sale'),
    path('inventory/', views.inventory, name='inventory'),
    path('report/', views.report, name='report'),
    path('report/<int:report_id>/', views.report_result, name='report-result'),
]
