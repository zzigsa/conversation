from django.db.models import Q
from django.http import Http404
from django.shortcuts import redirect, reverse, render
from django.views.generic import View
from django.views.generic import DetailView, ListView
from users import models as user_models
from . import models


def go_conversation(request, a_pk, b_pk):
    user_one = user_models.User.objects.get_or_none(pk=a_pk)
    user_two = user_models.User.objects.get_or_none(pk=b_pk)
    # print(user_one, user_two) user_one과 two에 url로 받은 숫자 들어가서 user로 변경되는거 확인
    if user_one is not None and user_two is not None:
        conversation = models.Conversation.objects.get(
            Q(participants=user_one) & Q(participants=user_two)
        )
        return redirect(reverse("conversations:detail", kwargs={"pk": conversation}))
        """
        try:
            conversation = models.Conversation.objects.get(
                Q(participants=user_one) & Q(participants=user_two)
            )   
            print('bye')
            # print(conversation) 얘가 안 뜸 try문 안으로는 들어왔는데 밖으로 못나감
        except models.Conversation.DoesNotExist:
            conversation = models.Conversation.objects.create()
            # print(conversation) 내가 만든 conversation명(one, two)
            conversation.participants.add(user_one, user_two)
        # return render(request, 'conversation_detail.html', {'conversation':conversation})
        return redirect(reverse("conversations:detail", kwargs={"pk": conversation}))
        """


class ConversationDetailView(DetailView):
    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        conversation = models.Conversation.objects.get_or_none(pk=pk)
        if not conversation:
            raise Http404()
        return render(
            self.request,
            "conversations/conversation_detail.html",
            {"conversation": conversation},
        )

    def post(self, *args, **kwargs):
        message = self.request.POST.get("message", None)
        pk = kwargs.get("pk")
        conversation = models.Conversation.objects.get_or_none(pk=pk)
        if not conversation:
            raise Http404()
        if message is not None:
            models.Message.objects.create(
                message=message, user=self.request.user, conversation=conversation
            )
        return redirect(reverse("conversations:detail", kwargs={"pk": pk}))

