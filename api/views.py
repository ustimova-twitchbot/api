from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
from api.models import Comment, User, Channel
from datetime import datetime
import requests
from django.views.decorators.csrf import csrf_exempt

#получить все комментарии/один комментарий (+создать/удалить)
@csrf_exempt
def get_comments(request, comment_id=None):
    if request.method == 'GET':
        if not comment_id:
            response = [model_to_dict(x) for x in Comment.objects.all()]
        else:
            response = Comment.objects.get(id=comment_id)
        return HttpResponse(response)

    elif request.method == 'POST':
        user = request.POST.get('user')
        channel = request.POST.get('channel')
        text = request.POST.get('text')
        new_comment = Comment(
            user=User.objects.get(name=user), 
            channel=Channel.objects.get(name=channel), 
            text=text
            )
        new_comment.save()
        return HttpResponse('')

    elif request.method == 'DELETE':
        Comment.objects.get(id=comment_id).delete()
        return HttpResponse('')


#получить комментарии по пользователю
def get_comments_by_user(request, user_name):
    response = [model_to_dict(x) for x in Comment.objects.filter(user__name=user_name)]
    return HttpResponse(response)

#получить комментарии по каналу
def get_comments_by_channel(request, channel_name):
    response = [model_to_dict(x) for x in Comment.objects.filter(channel__name=channel_name)]
    return HttpResponse(response)

#получить комментарий по дате
def get_comments_by_date(request, date):
    date_object = datetime.strptime(str(date), '%Y%m%d').date()
    response = [model_to_dict(x) for x in Comment.objects.filter(date__date=date_object)]
    return HttpResponse(response)

