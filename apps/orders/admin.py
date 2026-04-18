from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_price', 'get_item_count', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['user__username', 'user__email', 'id']
    readonly_fields = ['created_at', 'get_order_summary']
    fieldsets = (
        ('Order Information', {
            'fields': ('user', 'status', 'created_at')
        }),
        ('Order Summary', {
            'fields': ('total_price', 'get_order_summary'),
            'classes': ('collapse',)
        }),
    )
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    actions = ['mark_as_confirmed', 'mark_as_delivered']

    def get_item_count(self, obj):
        return obj.items.count()
    get_item_count.short_description = 'Items'

    def get_order_summary(self, obj):
        summary = f"<b>Order ID:</b> {obj.id}<br/>"
        summary += f"<b>Customer:</b> {obj.user.get_full_name() or obj.user.username}<br/>"
        summary += f"<b>Email:</b> {obj.user.email}<br/>"
        summary += f"<b>Total Items:</b> {obj.items.count()}<br/>"
        summary += f"<b>Total Amount:</b> ${obj.total_price:.2f}<br/>"
        summary += f"<b>Status:</b> {obj.get_status_display()}<br/>"
        summary += f"<b>Order Date:</b> {obj.created_at.strftime('%B %d, %Y at %I:%M %p')}<br/>"
        return summary
    get_order_summary.short_description = 'Order Summary'
    get_order_summary.allow_tags = True

    def mark_as_confirmed(self, request, queryset):
        updated = queryset.update(status='confirmed')
        self.message_user(request, f'{updated} order(s) marked as confirmed.')
    mark_as_confirmed.short_description = 'Mark selected orders as confirmed'

    def mark_as_delivered(self, request, queryset):
        updated = queryset.update(status='delivered')
        self.message_user(request, f'{updated} order(s) marked as delivered.')
    mark_as_delivered.short_description = 'Mark selected orders as delivered'
