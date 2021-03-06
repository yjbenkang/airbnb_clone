import datetime
from django import template
from reservations import models as reservation_models
from django.core.exceptions import MultipleObjectsReturned

register = template.Library()


@register.simple_tag
def is_booked(room, day):
    if day.number == 0:
        return
    try:
        date = datetime.datetime(year=day.year, month=day.month, day=day.number)
        booked_day = reservation_models.BookedDay.objects.get(
            day=date, reservation__room=room
        )
        return True
    except MultipleObjectsReturned:
        return True
    except reservation_models.BookedDay.DoesNotExist:
        return False