from django.shortcuts import render, redirect , get_object_or_404
from .models import Room, Message
from django.contrib.auth.decorators import login_required
# Create your views here.

def room_list(request):
    room = Room.objects.all()
    messages = Message.objects.all()
    username = request.user.username
    return render(request , "chat/room_list.html" , {'room' : room , 'messages' : messages , "username": username})


def HomeView(request):
    if request.method == 'POST' : 
        username = request.POST.get('username') 
        room = request.POST.get('room')
        try:
           existing_room = Room.objects.get(room_name__icontains = room)
        except Room.DoesNotExist:
           r = Room.objects.create(room_name = room)
        return redirect('chat:room' ,room_name = room ,  username = username )
    return render(request , 'chat/home.html')



# def room_view(request , room_name , username ):
#     room = get_object_or_404(Room , room_name = room_name )
#     messages = Message.objects.filter(room = room ,).order_by('id')
#     context = {
#         'room' : room , 
#         'messages' : messages , 
#         "user": username,
#     }
#     return render(request, 'chat/room.html', context)


@login_required
def room_view(request, room_name, username):
    room = get_object_or_404(Room, room_name=room_name)
    messages = Message.objects.filter(room=room).order_by('id')
    context = {
        'room': room,
        'messages': messages,
        # 'user': username,
        'room_name': room_name  # Передаем room_name в контекст
    }
    return render(request, 'chat/room.html', context)
