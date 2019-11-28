from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    """ Conversation model Definition """

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        nickname = []
        for user in self.participants.all():
            nickname.append(user.nickname)
        return ", ".join(nickname)  # 닉네임, 닉네임 대화창이 만들어졌음을 보여줌

    def count_messages(self):  # 메세지 갯수 보여줌
        return self.messages.count()  # messages가 conversation을 뽀링키로 갖고 있어서 꺼내쓸 수 있음

    count_messages.short_description = "Number of Messages"

    def count_participants(self):  # 참여인원 수
        return self.participants.count()

    count_participants.short_description = "Number of Participants"


class Message(core_models.TimeStampedModel):

    """ Message model Definition """

    message = models.TextField()  # 메세지를 텍스트필드로 생성
    # user랑 conversation을 뽀링키로 연결했기 때문에 user랑 conversation에서 message를 쓸 수 있음
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )  # CASCADE: User를 없애면 message도 같이 없어짐
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )  # conversation을 없애면 message도 같이 없어짐

    def __str__(self):
        return f"{self.user} says: {self.message}"

