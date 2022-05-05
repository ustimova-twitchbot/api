from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.get_comments, name='get_comments'),
    path('comments/<int:comment_id>/', views.get_comments, name='get_comments_by_id'),
    path('comments/user/<str:user_name>/', views.get_comments_by_user, name='get_comments_by_user'),
    path('comments/channel/<str:channel_name>/', views.get_comments_by_channel, name='get_comments_by_channel'),
    path('comments/date/<int:date>/', views.get_comments_by_date, name='get_comments_by_date'),
]