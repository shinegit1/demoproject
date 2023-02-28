from django.contrib import admin
from myapp.models import Contact


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    class Meta:
        model = Contact
        fields = ['__all__']
    list_display = ['id', 'name', 'age']