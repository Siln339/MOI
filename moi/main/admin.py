from django.contrib import admin
from .models import Image, Placemark, Type, Route

db_models = [Image, Placemark, Type, Route]
for model in db_models:
    admin.site.register(model) 