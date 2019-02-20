from django.core.management.base import BaseCommand
from booking.management.commands.private import create_Rooms, create_name, create_capacity, create_projector

class Command(BaseCommand):

    def handle(self, *args, **options):
        create_Rooms()
        self.stdout.write(self.style.SUCCESS("Successfully populated Rooms "))
