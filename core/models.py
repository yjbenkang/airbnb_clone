from django.db import models


class TimeStampedModel(models.Model):

    """Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    # absract model이란 model이지만 데이터베이스에는 나타나지 않는 model
    # 대다스ㅜ의 absrcat model은 확장을 하려고 사용한다.
