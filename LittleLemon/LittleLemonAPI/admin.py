from django.contrib import admin
from .models import Category, MenuItem, Cart, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
    search_fields = ['title', 'name']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'category', 'featured']
    list_filter = ['category', 'featured']
    search_fields = ['title']
    list_editable = ['featured']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'menuitem', 'quantity', 'unit_price', 'price']
    list_filter = ['user']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'delivery_crew', 'status', 'total', 'date']
    list_filter = ['status', 'date', 'delivery_crew']
    search_fields = ['user__username']
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'menuitem', 'quantity', 'price']
    list_filter = ['order']
