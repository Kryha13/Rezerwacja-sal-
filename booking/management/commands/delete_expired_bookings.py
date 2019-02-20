from django.core.management.base import BaseCommand
from django.utils import timezone
from booking.models import Booked


class Command(BaseCommand):
    help = 'Deletes expired rows'

    def handle(self, *args, **options):
        now = timezone.now()
        Booked.objects.filter(booked_to__lt=now).delete()
        self.stdout.write(self.style.SUCCESS("Successfully deleted expired bookings "))
