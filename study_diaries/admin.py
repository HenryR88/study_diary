from django.contrib import admin

from .models import Topic, Entry, Document

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Document)

