from django.contrib import admin
from .models import Result

#register result in /admin
class ResultAdmin(admin.ModelAdmin):
      list_display = ['search','result','found']

admin.site.register(Result,ResultAdmin)
