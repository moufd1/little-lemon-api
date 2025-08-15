from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create superuser and test users for Little Lemon API'

    def handle(self, *args, **options):
        # Create superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(
                self.style.SUCCESS('Successfully created superuser "admin" with password "admin123"')
            )
        else:
            self.stdout.write('Superuser admin already exists')

        # Create test manager
        if not User.objects.filter(username='manager1').exists():
            manager = User.objects.create_user('manager1', 'manager1@example.com', 'password123')
            from django.contrib.auth.models import Group
            manager_group = Group.objects.get(name='Manager')
            manager_group.user_set.add(manager)
            self.stdout.write(
                self.style.SUCCESS('Successfully created manager "manager1" with password "password123"')
            )
        else:
            self.stdout.write('Manager manager1 already exists')

        # Create test delivery crew
        if not User.objects.filter(username='delivery1').exists():
            delivery = User.objects.create_user('delivery1', 'delivery1@example.com', 'password123')
            from django.contrib.auth.models import Group
            delivery_group = Group.objects.get(name='Delivery crew')
            delivery_group.user_set.add(delivery)
            self.stdout.write(
                self.style.SUCCESS('Successfully created delivery crew "delivery1" with password "password123"')
            )
        else:
            self.stdout.write('Delivery crew delivery1 already exists')

        # Create test customer
        if not User.objects.filter(username='customer1').exists():
            User.objects.create_user('customer1', 'customer1@example.com', 'password123')
            self.stdout.write(
                self.style.SUCCESS('Successfully created customer "customer1" with password "password123"')
            )
        else:
            self.stdout.write('Customer customer1 already exists')

        self.stdout.write(
            self.style.SUCCESS('All users are ready!')
        )
