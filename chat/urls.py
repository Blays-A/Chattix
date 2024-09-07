from django.urls import path
from . import views


app_name = 'chat'
urlpatterns = [
    path('' , views.HomeView , name='home') , 
    # path('room/<int:room_id>/', views.room_view, name='room'),
    path("<str:room_name>/<str:username>/", views.room_view, name="room"),
    path('list_of_rooms/' , views.room_list , name = 'room_list')
]