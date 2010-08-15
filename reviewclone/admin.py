from django.contrib import admin

from models import Review, Item, Relation, Simular

class ReviewAdmin(admin.ModelAdmin):
    pass
admin.site.register(Review, ReviewAdmin)

class ItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(Item, ItemAdmin)
 
class RelationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Relation, RelationAdmin) 

class SimularAdmin(admin.ModelAdmin):
    pass
admin.site.register(Simular, RelationAdmin)
