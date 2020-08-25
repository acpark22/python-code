"""Defines URL patterns for stock_trackers."""

from django.urls import path
from .import views

app_name= 'stock_trackers'
urlpatterns= [
    # Homepage
    path('', views.index, name='index'),
    # Page that shows all stocks
    path('stocks/', views.stocks, name='stocks'),
    # Page for adding a new stock
    path('new_stock/', views.new_stock, name= 'new_stock'),
    # Notes page for single stock
    path('stocks/<int:stock_id>/', views.stock, name= 'stock'),
    # Page for adding a new notes
    path('new_entry/<int:stock_id>/', views.new_entry, name= 'new_entry'),
    # Page for editing notes.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name= 'edit_entry'),
    ]

