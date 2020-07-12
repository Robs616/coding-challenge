from django.contrib import admin

from .models import BuzzwordCategory, Buzzword

#register buzzword, buzzwordcategory in /admin
class BuzzwordAdmin(admin.ModelAdmin):
      list_display = ['name','description','category']

admin.site.register(BuzzwordCategory)
admin.site.register(Buzzword,BuzzwordAdmin)



