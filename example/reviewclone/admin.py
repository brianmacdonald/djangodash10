from django.contrib import admin

from reviewclone.models import Review, Item, Relation, Similar

class ReviewAdmin(admin.ModelAdmin):
    pass
admin.site.register(Review, ReviewAdmin)

class ItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(Item, ItemAdmin)
 
class RelationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Relation, RelationAdmin) 

class SimilarAdmin(admin.ModelAdmin):
    pass
admin.site.register(Similar, RelationAdmin)
