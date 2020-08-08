from django.contrib import admin
from .models import Project, Course, Session

# Register your models here.
admin.site.register(Project)
admin.site.register(Course)
admin.site.register(Session)

