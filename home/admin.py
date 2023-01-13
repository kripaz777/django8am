from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "My Ecommerce Shop"
class ProductA(admin.ModelAdmin):
    list_display = ('name', 'price','category','subcategory','label','stock')
    list_filter = ('category','label','stock')
    search_fields = ('title','description')


class Cart_list(admin.ModelAdmin):
    list_display = ('username', 'items','quantity','total','checkout')
    list_filter = ('checkout',)
    search_fields = ('username','slug')

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Ad)
admin.site.register(Brand)
admin.site.register(Slider)
admin.site.register(Product,ProductA)
admin.site.register(ProductReview)
admin.site.register(Cart,Cart_list)
admin.site.register(Review)