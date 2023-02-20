from django.urls import path
from myapp.views import home_page

urlpatterns = [
    path('', home_page, name='home'),
]