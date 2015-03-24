from django.contrib import admin

# Register your models here.
from models import Note, Tag, Folder

admin.site.register(Note)
admin.site.register(Tag)
admin.site.register(Folder)