from django.views.generic import ListView
from myapp.models import Contact


class ContactListView(ListView):
    model = Contact
    template_name = 'contact_list.html'
