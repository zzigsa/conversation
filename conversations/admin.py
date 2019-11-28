from django.contrib import admin
from . import models

# user가 보낸 message
@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """ Message Admin Definition """

    # admin에 말한사람:대화내용, 보낸시간 보여줌
    list_display = ("__str__", "created")


# message가모여 대화
@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """ Conversation Admin Definition """

    # admin에 대화참여인 메세지 갯수, 참여인수 보여줌
    list_display = ("__str__", "count_messages", "count_participants")
