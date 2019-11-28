from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)  # model을 생성하면 현재 날짜, 시간 넣어줌
    updated = models.DateTimeField(auto_now=True)  # model을 저장하면 넣어줌

    # core의 model이 db에 등록되는게 아니라 이 model을 사용하는 model이 등록되게 만들어야 함
    # Meta class를 통해 그렇게 만들어주자
    class Meta:
        # abastract는 db에 등록되지 않으며 확장을 위해 사용
        abstract = True
