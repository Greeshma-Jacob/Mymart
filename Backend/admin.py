from django.contrib import admin

# Register your models here.
from Backend.models import categorydb,productdb
from webapp.models import contactdb
admin.site.register(categorydb)
admin.site.register(productdb)
admin.site.register(contactdb)
