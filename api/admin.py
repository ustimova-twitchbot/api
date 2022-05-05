from django.contrib import admin
from .models import User, Channel, Comment

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class ChannelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'date', 'user', 'channel')

admin.site.register(User, UserAdmin)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(Comment, CommentAdmin)
