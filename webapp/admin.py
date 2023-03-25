from django.contrib import admin
from webapp.models import Review, Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'description', 'image')
    list_filter = ('id', 'title', 'category', 'description', 'image')
    search_fields = ('title', 'category', 'description', 'image')
    fields = ('title', 'category', 'description', 'image')
    readonly_fields = ('id',)


admin.site.register(Product, ProductAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'product', 'text', 'score')
    list_filter = ('id', 'author', 'product', 'text', 'score')
    search_fields = ('author', 'product', 'text', 'score')
    fields = ('author', 'product', 'text', 'score')
    readonly_fields = ('id',)


admin.site.register(Review, ReviewAdmin)