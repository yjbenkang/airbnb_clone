from datetime import datetime
from django.shortcuts import render
from . import models


def all_rooms(request):
    print(request.GET)
    all_rooms = models.Room.objects.all()[10:20]
    return render(request, "rooms/home.html", context={"rooms": all_rooms})
