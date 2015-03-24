from django.contrib import admin
from django.db.models import get_models, get_app

# Smarter way to register all models for an app
for model in get_models(get_app('notes')):
    # If you need to customise or
    # have duplicate models exclude them
    admin.site.register(model)