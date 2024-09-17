from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/submit/', views.submit_transaction, name='submit_transaction'),
    path('api/history/', views.transaction_history, name='transaction_history'),
]
