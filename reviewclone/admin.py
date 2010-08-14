from django.contrib import admin

from models import Review, Item

class UnitAdmin(admin.ModelAdmin):
    pass
admin.site.register(Review, UnitAdmin)

class ItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(Item, ItemAdmin)
 
