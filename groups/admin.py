from django.contrib import admin
from . import models
# Register your models here.

class GroupMembeInline(admin.TabularInline):
    Model = models.GroupMember

admin.site.register(models.Group)
