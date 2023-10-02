from django.contrib import admin
from .models import Credit
from .models import user
from .models import feedback
# Register your models here.
admin.site.register(Credit)
admin.site.register(feedback)

admin.site.register(user)
