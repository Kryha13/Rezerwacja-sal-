from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from booking.models import Room, Booked
# Create your views here.


def room(request):
    room = Room.objects.order_by('id')

    ctx = {
        'room': room
    }
    return render(request, 'main_page.html', ctx)


@csrf_exempt
def new_room(request):
    if request.method == 'POST':
        name = request.POST.get('room_name')
        capacity = request.POST.get('room_capacity')
        projector = request.POST.get('projector')

        r = Room()
        r.name = name
        r.capacity = capacity
        r.projector = projector
        r.save()
    return render(request, 'new_room.html', {'new_room': new_room})

@csrf_exempt
def delete_room(request):
    if request.method == 'GET':
        room = Room.objects.all()
        ctx = {
            'room': room
        }
        return render(request, 'delete_room.html', ctx)
    else:
        name = request.POST.get('room_name')
        r = Room.objects.get(name=name)
        r.delete()

    return render(request, 'delete_room.html', {'delete_room': delete_room})


@csrf_exempt
def room_details(request, room_id):
    room = Room.objects.get(pk=room_id)
    ctx = {
        'room': room
    }
    return render(request, 'room_details.html', ctx)

@csrf_exempt
def modify_room(request, room_id):
    if request.method == 'GET':
        room = Room.objects.get(pk=room_id)
        ctx = {
            'room': room,
        }
        return render(request, 'modify_room.html', ctx)

    else:
        room = Room.objects.get(pk=room_id)
        name = request.POST.get('room_name')
        capacity = request.POST.get('room_capacity')
        projector = request.POST.get('projector')

        room.name = name
        room.capacity = capacity
        room.projector = projector
        room.save()
        ctx = {
            'room': room,
        }

    return render(request, 'modify_room.html', ctx, {'modify_room': new_room})

@csrf_exempt
def book_room(request, room_id):
    if request.method == 'GET':
        room = Room.objects.get(pk=room_id)
        book = Booked.objects.filter(room_id=room_id)
        ctx = {
            'room': room,
            'book': book,
        }
        return render(request, 'book_room.html', ctx)
    else:
        room = Room.objects.get(pk=room_id)
        book = Booked.objects.filter(room_id=room_id)
        book_from = request.POST.get('booked_from')
        book_to = request.POST.get('booked_to')

        b = Booked()
        b.booked_from = book_from
        b.booked_to = book_to
        b.room_id = room_id
        b.save()
        ctx = {
            'room': room,
            'book': book,
        }

    return render(request, 'book_room.html', ctx, {'book_room': new_room})

