from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument("--number", help="How many users do you want to create")

    def handle(self, *args, **options):
        amenities = [
            "에어컨",
            "알람시계",
            "발코니",
            "화장실",
            "욕조",
            "린넨 침대",
            "케이블 TV",
            "이산화탄소 탐지기",
            "의자",
            "어린이 시설",
            "커피머신",
            "취사시설",
            "조리기구",
            "식기세척기r",
            "더블베드,
            "스위트룸",
            "주차 무료",
            "무료 무선인터넷",
            "냉장고",
            "냉장/냉동고",
            "헤어 드라이기",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))