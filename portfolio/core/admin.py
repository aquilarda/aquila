from django.contrib import admin
from .models import About, Project, Blog, UrlModel

admin.site.register(About)
admin.site.register(Project)
admin.site.register(Blog)
admin.site.register(UrlModel)
