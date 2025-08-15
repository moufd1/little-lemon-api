from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Create test users for Little Lemon API'

    def handle(self, *args, **options):
        # Create manager user
        manager_user, created = User.objects.get_or_create(
            username='manager1',
            defaults={
                'email': 'manager1@littlelemon.com',
                'first_name': 'Manager',
                'last_name': 'One'
            }
        )
        if created:
            manager_user.set_password('manager123')
            manager_user.save()
            manager_group = Group.objects.get(name='Manager')
            manager_group.user_set.add(manager_user)
            self.stdout.write(f'Created manager: {manager_user.username}')

        # Create delivery crew user
        delivery_user, created = User.objects.get_or_create(
            username='delivery1',
            defaults={
                'email': 'delivery1@littlelemon.com',
                'first_name': 'Delivery',
                'last_name': 'One'
            }
        )
        if created:
            delivery_user.set_password('delivery123')
            delivery_user.save()
            delivery_group = Group.objects.get(name='Delivery crew')
            delivery_group.user_set.add(delivery_user)
            self.stdout.write(f'Created delivery crew: {delivery_user.username}')

        # Create customer users
        for i in range(1, 3):
            customer_user, created = User.objects.get_or_create(
                username=f'customer{i}',
                defaults={
                    'email': f'customer{i}@littlelemon.com',
                    'first_name': 'Customer',
                    'last_name': f'{i}'
                }
            )
            if created:
                customer_user.set_password('customer123')
                customer_user.save()
                self.stdout.write(f'Created customer: {customer_user.username}')

        self.stdout.write(
            self.style.SUCCESS('Test users created successfully!')
        )
