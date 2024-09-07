from django.urls import path , include
from . import views

app_name = 'users'

urlpatterns =[
    path('' , include('django.contrib.auth.urls') ) , 
    path('profile/<str:username>/', views.profile, name='profile'),
    path('register/' , views.register , name = 'register'), 
    path('edit_profile/<int:id>/' , views.edit_profile , name='edit_profile') , 
    # path('all_profiles/' ,views.all_profiles , name='all_profiles')
]