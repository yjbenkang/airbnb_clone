from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This command creates amenities!"

    """     def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many times do you want me to tell you that I love you?"
        )
        """

    def handle(self, *args, **options):
        amenities = [
            "에어컨",
            "알람시계",
            "발코니",
            "화장실",
            "욕조",
            "린넨 침대",
            "주유시설",
            "케이블 TV",
            "일산화탄소 감지기",
            "의자",
            "어린이 시설",
            "커피머신",
            "취사시설",
            "조리기구 및 주방 용품",
            "식기세척기",
            "더블 베드",
            "스위트룸",
            "무료주차",
            "무료 무선인터넷",
            "냉동고",
            "냉장/냉장고",
            "골프용품",
            "헤어 드라이기",
            "히터",
            "온수",
            "실내수영장",
            "다리미판",
            "전자렌지",
            "실외수영장",
            "실외 테니스장",
            "O오븐",
            "퀸 사이즈 침대",
            "레스토랑",
            "쇼핑몰",
            "샤워룸",
            "연기 감지기",
            "소파",
            "스테레오",
            "화장실",
            "타월",
            "TV",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))