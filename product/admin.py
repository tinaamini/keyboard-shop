from django.contrib import admin
from .models import BaseProducts,Attributes,Value,ProductImage
from django.utils.html import format_html
# Register your models here.
class ValueAdmin(admin.ModelAdmin):
    list_display = ('product', 'attribute', 'value')
    search_fields = ('value',)
    list_filter = ('product', 'attribute')

class ImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    image_tag.short_description = 'ProductImage'
    list_display = ['product','image_tag', ]




admin.site.register(BaseProducts)
admin.site.register(Attributes)
admin.site.register(ProductImage,ImageAdmin)
admin.site.register(Value,ValueAdmin)
