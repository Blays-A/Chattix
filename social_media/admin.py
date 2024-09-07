from django.contrib import admin
from .models import Video , Comment
# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title' , 'caption' , )
    prepopulated_fields = {'slug' : ('title',)}

admin.site.register(Video , VideoAdmin)
admin.site.register(Comment)