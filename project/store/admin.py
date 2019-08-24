from django.contrib import admin
from .models import Store
from .models import Client
# Register your models here.

admin.site.register(Store)
admin.site.register(Client)