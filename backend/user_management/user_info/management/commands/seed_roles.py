from django.core.management.base import BaseCommand
from user_info.models import Role

class Command(BaseCommand):
    help = 'Seed the database with initial roles'

    def handle(self, *args, **options):
        roles_data = [
            {'role_type': 'owner', 'description': 'Full permissions'},
            {'role_type': 'member', 'description': 'Specific permissions'},
            {'role_type': 'viewer', 'description': 'Read permission'},
        ]

        for role_data in roles_data:
            role, created = Role.objects.get_or_create(
                role_type=role_data['role_type'],
                defaults={'description': role_data['description']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created role: {role.role_type}'))
            else:
                self.stdout.write(f'Role already exists: {role.role_type}')

        self.stdout.write(self.style.SUCCESS('Roles seeded successfully!'))
