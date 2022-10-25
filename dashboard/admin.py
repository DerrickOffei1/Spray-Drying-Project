from django.contrib import admin
from . models import Database
# Register your models here.
class DatabaseAdmin(admin.ModelAdmin):
    list_display = ("Temperature", "Maltodextrin", "FlowRate", "Yield", "MoistureContent", "ColorChange", "R")
admin.site.register(Database, DatabaseAdmin)
	
     	
     
    
    
    
     