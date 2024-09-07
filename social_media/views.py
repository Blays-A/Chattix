from django.shortcuts import render , get_object_or_404 , redirect
from .models import Video , Comment
from django.contrib.auth.decorators import login_required
from chat.models import Message , Room 
from users.models import Profile
from django.contrib.auth.models import User
from .forms import CommentForm , NewVideoForm
# Create your views here. 
@login_required(login_url = "users:login")
def index(request):
    video = Video.objects.all()
    return render(request , "social_media/index.html" , {'video' : video , })


def detail(request , id , slug):
    video = get_object_or_404( Video , id = id , slug = slug ) 
    comment = Comment.objects.filter(video = video)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.video = video
            new_comment.author = request.user
            new_comment.save()
            return redirect('social_media:video_detail' ,  video.id , video.slug)
    else:
        form = CommentForm()
    return render(request , 'social_media/video_detail.html' , {'video' : video , 'comment' : comment , 'form' : form })

# def new_video(request , id):
#     user = get_object_or_404(User , id = id)
#     if request.method=='POST':
#         form = NewVideoForm()
#         if form.is_valid():
#             new_comment = form.save(commit=False)
#             new_comment.author = user
#             new_comment.save()
#             return redirect('users:profile' ,  user.id)
#     else:
#         form = NewVideoForm()
#     return render(request , 'social_media/new_video.html' , {'form' : form })



def new_video(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = NewVideoForm(request.POST , request.FILES)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = user
            new_comment.save()
            return redirect('users:profile', user.username)
    else:
        form = NewVideoForm()
    return render(request, 'social_media/new_video.html', {'form': form})



# def all_your_comments(request , id):
#     user = get_object_or_404(User , id = id)
#     comment = Comment.objects.filter( author = user )
#     video = Video.objects.filter(comment__in = comment)
#     return render(request , 'social_media/all_your_comments.html' , {'comment' : comment ,  'user' : user , 'video' : video})


def all_your_comments(request , id):
    user = get_object_or_404(User , id = id)
    comment = Comment.objects.filter( author = user ).select_related('video')
    return render(request , 'social_media/all_your_comments.html' , {'comment' : comment ,  'user' : user })

def del_comment(request, id):
    comment = get_object_or_404(Comment , id = id)
    video = get_object_or_404(Video , comment = comment)
    comment.delete()
    return redirect('social_media:all_your_comments' , request.user.id)

def del_video(request , video_id , user_id):
    user = get_object_or_404(User , id = user_id)
    video = get_object_or_404(Video , id = video_id ,  author = user)
    video.delete()
    return redirect('users:profile' , user.username )