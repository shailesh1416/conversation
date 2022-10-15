from django.shortcuts import render
from .models import Conversation, Chats
# Create your views here.


def practice(request):
    conversations = Conversation.objects.all()
    firstConnversationId = conversations.first().id
    chats = Chats.objects.filter(conversation=firstConnversationId).order_by('sentence_no')
    characters = chats.values('name').distinct()
    names = []
    for character in characters:
        names.append(character['name'])
    return render(request, 'practice.html', {'chats': chats, 'names': characters,'conversations':conversations})

def showConversation(request,pk):
    conversations = Conversation.objects.all()
    chats = Chats.objects.filter(conversation=pk).order_by('sentence_no')
    characters = chats.values('name').distinct()
    names = []
    for character in characters:
        names.append(character['name'])
    return render(request, 'practice.html', {'chats': chats, 'names': characters,'conversations':conversations})