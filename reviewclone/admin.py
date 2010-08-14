from django.contrib import admin

from models import Review, Item, Relation

class ReviewAdmin(admin.ModelAdmin):
    pass
admin.site.register(Review, ReviewAdmin)

class ItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(Item, ItemAdmin)
 
class RelationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Relation, RelationAdmin) 
