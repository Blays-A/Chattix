from django.shortcuts import render , redirect , get_object_or_404
from django .contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from social_media.models import Video
from django.contrib.auth import login
from .forms import ProfileForm
from .models import Profile
# Create your views here.

# def profile(request):
#     return render(request , 'registration/profile.html' )


def profile(request , username ):
    user = get_object_or_404(User , username = username)
    video = Video.objects.filter(author = user)
    return render(request, 'registration/profile.html' , {'user' :  user , 'video' : video})

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data= request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('social_media:all_videos')
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)


def edit_profile(request , id):
    user = get_object_or_404(User , id = id)
    profile = get_object_or_404(Profile , user = user)
    if request.method == 'POST':
        form = ProfileForm(request.POST , request.FILES , instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile' ,  user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request , 'registration/edit_profile.html' , {'form' : form , 'user' : user})


# def all_profiles(request):
#     profiles = Profile.objects.all()
#     return render(request, 'registration/profile_list.html', {'profiles': profiles})