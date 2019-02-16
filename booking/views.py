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
