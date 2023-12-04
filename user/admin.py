from django.contrib import admin

# Register your models here.
from .models import OlxUser, OlxUserProfile


admin.site.register(OlxUser)
admin.site.register(OlxUserProfile)