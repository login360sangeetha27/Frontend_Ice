from django.contrib import admin
from django.utils.html import format_html
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'get_description_preview', 'get_image_preview', 'created_at']
    list_filter = ['created_at', 'price']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'get_product_image_display']
    fieldsets = (
        ('Product Information', {
            'fields': ('name', 'description', 'price')
        }),
        ('Media', {
            'fields': ('image', 'get_product_image_display')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    
    def get_description_preview(self, obj):
        """Display truncated description"""
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    get_description_preview.short_description = 'Description'
    
    def get_image_preview(self, obj):
        """Display product image thumbnail"""
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 5px;" />',
                obj.image
            )
        return "No image"
    get_image_preview.short_description = 'Image'
    
    def get_product_image_display(self, obj):
        """Display product image at full size in detail view"""
        if obj.image:
            return format_html(
                '<img src="{}" width="300" style="border-radius: 5px; margin-top: 10px;" />',
                obj.image
            )
        return "No image available"
    get_product_image_display.short_description = 'Product Image Preview'
