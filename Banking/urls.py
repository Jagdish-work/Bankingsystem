from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('transaction-history/', views.transaction_history, name='transaction_history'),
    path('transfer-money/', views.transfer_money, name='transfer_money'),
    path('accounts/<int:account_id>/', views.account_detail, name='account_detail'),
]