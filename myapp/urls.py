from django.urls import path
from myapp.views import ContactListView

urlpatterns = [
    path('', ContactListView.as_view(), name='home'),
]