# In urls.py
from django.urls import path
from .views import add_bill_reminder, bill_reminder_list, delete_bill_reminder, bills_home

urlpatterns = [
    path('add_bill_reminder/', add_bill_reminder, name='add_bill_reminder'),
    path('bill_reminder_list/', bill_reminder_list, name='bill_reminder_list'),
    path('delete_bill_reminder/<int:reminder_id>/', delete_bill_reminder, name='delete_bill_reminder'),
    path('bills_home/', bills_home, name='bills_home'),
]
