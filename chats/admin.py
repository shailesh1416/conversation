from django.contrib import admin
from .models import Conversation, Chats
# Register your models here.


class ConversationAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


class ChatsAdmin(admin.ModelAdmin):
    list_display = ['name', 'sentence','sentence_no']
    list_filter = ['conversation']



admin.site.register(Conversation, ConversationAdmin)
admin.site.register(Chats, ChatsAdmin)

