from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from LittleLemonAPI.models import Category, MenuItem
from decimal import Decimal

class Command(BaseCommand):
    help = 'Create sample data for Little Lemon API'

    def handle(self, *args, **options):
        # Create categories
        categories = [
            'Appetizers',
            'Main Course',
            'Desserts',
            'Beverages',
        ]
        
        for cat_name in categories:
            category, created = Category.objects.get_or_create(name=cat_name)
            if created:
                self.stdout.write(f'Created category: {cat_name}')

        # Create menu items
        menu_items = [
            # Appetizers
            {'title': 'Bruschetta', 'price': Decimal('8.99'), 'category': 'Appetizers', 'featured': True},
            {'title': 'Calamari Rings', 'price': Decimal('12.99'), 'category': 'Appetizers', 'featured': False},
            {'title': 'Greek Salad', 'price': Decimal('9.99'), 'category': 'Appetizers', 'featured': False},
            
            # Main Course
            {'title': 'Grilled Salmon', 'price': Decimal('24.99'), 'category': 'Main Course', 'featured': True},
            {'title': 'Chicken Parmesan', 'price': Decimal('19.99'), 'category': 'Main Course', 'featured': False},
            {'title': 'Beef Steak', 'price': Decimal('29.99'), 'category': 'Main Course', 'featured': True},
            {'title': 'Vegetarian Pizza', 'price': Decimal('16.99'), 'category': 'Main Course', 'featured': False},
            
            # Desserts
            {'title': 'Tiramisu', 'price': Decimal('7.99'), 'category': 'Desserts', 'featured': True},
            {'title': 'Chocolate Cake', 'price': Decimal('6.99'), 'category': 'Desserts', 'featured': False},
            {'title': 'Lemon Tart', 'price': Decimal('5.99'), 'category': 'Desserts', 'featured': False},
            
            # Beverages
            {'title': 'Fresh Orange Juice', 'price': Decimal('4.99'), 'category': 'Beverages', 'featured': False},
            {'title': 'Italian Coffee', 'price': Decimal('3.99'), 'category': 'Beverages', 'featured': True},
            {'title': 'House Wine', 'price': Decimal('8.99'), 'category': 'Beverages', 'featured': False},
        ]
        
        for item_data in menu_items:
            category = Category.objects.get(name=item_data['category'])
            menu_item, created = MenuItem.objects.get_or_create(
                title=item_data['title'],
                defaults={
                    'price': item_data['price'],
                    'category': category,
                    'featured': item_data['featured']
                }
            )
            if created:
                self.stdout.write(f'Created menu item: {item_data["title"]}')

        self.stdout.write(
            self.style.SUCCESS('Sample data created successfully!')
        )
