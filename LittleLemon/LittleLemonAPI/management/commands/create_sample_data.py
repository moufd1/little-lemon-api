from django.core.management.base import BaseCommand
from LittleLemonAPI.models import Category, MenuItem

class Command(BaseCommand):
    help = 'Create sample data for Little Lemon API'

    def handle(self, *args, **options):
        # Create categories
        categories_data = [
            {'title': 'Appetizers', 'slug': 'appetizers'},
            {'title': 'Main Dishes', 'slug': 'main-dishes'},
            {'title': 'Desserts', 'slug': 'desserts'},
            {'title': 'Beverages', 'slug': 'beverages'},
        ]

        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={'title': cat_data['title'], 'name': cat_data['title']}
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created category "{category.title}"')
                )

        # Create menu items
        appetizers = Category.objects.get(slug='appetizers')
        main_dishes = Category.objects.get(slug='main-dishes')
        desserts = Category.objects.get(slug='desserts')
        beverages = Category.objects.get(slug='beverages')

        menu_items_data = [
            {'title': 'Greek Salad', 'price': 12.50, 'category': appetizers, 'featured': True},
            {'title': 'Bruschetta', 'price': 8.99, 'category': appetizers, 'featured': False},
            {'title': 'Grilled Fish', 'price': 24.99, 'category': main_dishes, 'featured': True},
            {'title': 'Pasta Carbonara', 'price': 18.50, 'category': main_dishes, 'featured': False},
            {'title': 'Lemon Cake', 'price': 7.99, 'category': desserts, 'featured': True},
            {'title': 'Tiramisu', 'price': 9.50, 'category': desserts, 'featured': False},
            {'title': 'Lemonade', 'price': 4.99, 'category': beverages, 'featured': False},
            {'title': 'Coffee', 'price': 3.50, 'category': beverages, 'featured': False},
        ]

        for item_data in menu_items_data:
            item, created = MenuItem.objects.get_or_create(
                title=item_data['title'],
                defaults=item_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created menu item "{item.title}"')
                )

        self.stdout.write(
            self.style.SUCCESS('Sample data created successfully!')
        )
