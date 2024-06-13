from django.contrib import admin
from .models import Profile, Route, Type, Image 

db_models = [Profile, Route, Type, Image]
for model in db_models:
    admin.site.register(model)