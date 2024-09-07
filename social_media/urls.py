from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'social_media'

urlpatterns = [
    path('' , views.index , name='all_videos') ,
    path('<int:id>/<slug:slug>', views.detail, name='video_detail'),
    path('new_video/<int:id>/' , views.new_video , name='new_video') , 
    path('all_your_comments/<int:id>/' , views.all_your_comments , name='all_your_comments') ,
    path('del_comment/<int:id>/' , views.del_comment , name='del_comment') , 
    path('del_video/<int:video_id>/<int:user_id>/' , views.del_video , name='del_video')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
