from django.contrib import admin
from .models import Route, Type, Image

db_models = [Route, Type, Image]
for model in db_models:
    admin.site.register(model) 