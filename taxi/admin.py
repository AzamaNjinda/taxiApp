from django.contrib import admin
from .models import Credit
from .models import user
# Register your models here.
admin.site.register(Credit)

admin.site.register(user)
