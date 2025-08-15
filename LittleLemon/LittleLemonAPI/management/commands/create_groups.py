from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Create user groups for Little Lemon API'

    def handle(self, *args, **options):
        # Create Manager group
        manager_group, created = Group.objects.get_or_create(name='Manager')
        if created:
            self.stdout.write(
                self.style.SUCCESS('Successfully created "Manager" group')
            )
        else:
            self.stdout.write('Manager group already exists')

        # Create Delivery crew group
        delivery_group, created = Group.objects.get_or_create(name='Delivery crew')
        if created:
            self.stdout.write(
                self.style.SUCCESS('Successfully created "Delivery crew" group')
            )
        else:
            self.stdout.write('Delivery crew group already exists')

        self.stdout.write(
            self.style.SUCCESS('All groups are ready!')
        )
