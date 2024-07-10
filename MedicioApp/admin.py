from django.contrib import admin
from MedicioApp.models import Product
from MedicioApp.models import Branch
from MedicioApp.models import Contact
from MedicioApp.models import Appointment

# Register your models here.
admin.site.register(Product)
admin.site.register(Branch)
admin.site.register(Contact)
admin.site.register(Appointment)
