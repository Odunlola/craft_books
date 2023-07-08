from django.contrib import admin

from .models import Craft # import the Artist model from models.py
# Register your models here.

admin.site.register(Craft) # this line will add the model to the admin panel