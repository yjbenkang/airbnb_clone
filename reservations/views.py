import datetime
from django.http import Http404
from django.views.generic import View, ListView
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from rooms import models as room_models
from reviews import forms as review_forms
from . import models


class CreateError(Exception):
    pass


def click_reservation(request, room, year, month, day):
    try:
        date_obj = datetime.datetime(year, month, day)
        room = room_models.Room.objects.get(pk=room)
        booked_day = models.BookedDay.objects.get(day=date_obj, reservation__room=room)
        host = room.host
        if request.user == host:
            reservation = booked_day.reservation
            return redirect(
                reverse("reservations:detail", kwargs={"pk": reservation.pk})
            )
        else:
            raise CreateError()
    except (room_models.Room.DoesNotExist, CreateError):
        messages.error(request, "예약할 수 없습니다.")
        return redirect(reverse("core:home"))
    except models.BookedDay.DoesNotExist:
        first_num = 0
        second_num = 0
        first_same_day = models.BookedDay.objects.filter(day=date_obj)
        second_same_day = models.BookedDay.objects.filter(
            day=date_obj + datetime.timedelta(days=1)
        )
        if len(first_same_day) == 0:
            first_num = 0
        elif len(first_same_day) >= 1:
            first_num += 1
        if len(second_same_day) == 0:
            second_num = 0
        elif len(second_same_day) >= 1:
            second_num += 1
        reservation = models.Reservation.objects.create(
            guest=request.user,
            room=room,
            check_in=date_obj,
            check_out=date_obj + datetime.timedelta(days=1),
        )
        if first_num >= 1 or (first_num == 0 and second_num >= 1):
            booked_day1 = models.BookedDay.objects.create(
                day=date_obj, reservation=reservation
            )
            booked_day2 = models.BookedDay.objects.create(
                day=date_obj + datetime.timedelta(days=1), reservation=reservation
            )
        return redirect(reverse("reservations:detail", kwargs={"pk": reservation.pk}))


class ReservationDetailView(View):
    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        reservation = models.Reservation.objects.get_or_none(pk=pk)
        if not reservation or (
            reservation.guest != self.request.user
            and reservation.room.host != self.request.user
        ):
            raise Http404()
        form = review_forms.CreateReviewForm()
        return render(
            self.request,
            "reservations/detail.html",
            {"reservation": reservation, "form": form},
        )


def edit_reservation(request, pk, verb):
    reservation = models.Reservation.objects.get_or_none(pk=pk)
    if not reservation or (
        reservation.guest != request.user and reservation.room.host != request.user
    ):
        raise Http404()
    if verb == "confirm":
        reservation.status = models.Reservation.STATUS_CONFIRMED
    elif verb == "cancel":
        reservation.status = models.Reservation.STATUS_CANCELED
        models.BookedDay.objects.filter(reservation=reservation).delete()
    elif verb == "pending":
        reservation.status = models.Reservation.STATUS_PENDING
    reservation.save()
    messages.success(request, "예약상태 변경이 완료되었습니다.")
    return redirect(reverse("reservations:detail", kwargs={"pk": reservation.pk}))


def show_reservations(request):
    user = request.user
    today = datetime.date.today()
    pending_reservations = models.Reservation.objects.filter(
        guest=user.pk, status="pending"
    )

    confirmed_reservations = models.Reservation.objects.filter(
        guest=user.pk, status="confirmed"
    )
    finished_reservations = []
    notyet_reservations = []
    for confirmed_reservation in confirmed_reservations:
        if confirmed_reservation.check_out < today:
            finished_reservations.append(confirmed_reservation)
        else:
            notyet_reservations.append(confirmed_reservation)

    canceled_reservations = models.Reservation.objects.filter(
        guest=user.pk, status="canceled"
    )
    return render(
        request,
        "reservations/reserved_rooms.html",
        {
            "pending_reservations": pending_reservations,
            "finished_reservations": finished_reservations,
            "canceled_reservations": canceled_reservations,
            "notyet_reservations": notyet_reservations,
        },
    )
