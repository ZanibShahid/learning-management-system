from django.contrib import admin
from lmsAdmin.models import User,SchoolClass
# Register your models here.

class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('id' ,'name')

admin.site.register(SchoolClass, SchoolClassAdmin)
