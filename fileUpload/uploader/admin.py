from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UploadedContent  # Import your model

# Register your model
admin.site.register(UploadedContent)
