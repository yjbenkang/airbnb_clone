from django.core.management.base import BaseCommand
from rooms.models import RoomType


class Command(BaseCommand):

    help = "This command creates many roomtypes"

    def add_arguments(self, parser):
        parser.add_argument("--number", help="How many roomtypes do you want to create")

    def handle(self, *args, **options):
        roomtypes = [
            "독채",
            "호텔",
            "쉐어하우스",
            "모텔",
            "호스텔",
            "오피스텔",
            "콘도",
        ]
        for f in roomtypes:
            RoomType.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(roomtypes)} roomtypes created!"))