from datetime import timezone

from django.conf import settings
from django.db import models

from account.models import User


class WayChoices(models.TextChoices):
    지하철 = '지하철'
    택시 = '택시'
    버스 = '버스'
    자차 = '자차'
    도보 = '도보'

class Board(models.Model):
    # 구 선택지 (폼에서 강남구를 선택하면 강남구가 db에 저장되도록)
    DISTRICT_CHOICES = (
        ('강남구', '강남구'),
        ('강동구', '강동구'),
        ('강북구', '강북구'),
        ('강서구', '강서구'),
        ('관악구', '관악구'),
        ('광진구', '광진구'),
        ('구로구', '구로구'),
        ('금천구', '금천구'),
        ('노원구', '노원구'),
        ('도봉구', '도봉구'),
        ('동대문구', '동대문구'),
        ('동작구', '동작구'),
        ('마포구', '마포구'),
        ('서대문구', '서대문구'),
        ('서초구', '서초구'),
        ('성동구', '성동구'),
        ('성북구', '성북구'),
        ('송파구', '송파구'),
        ('양천구', '양천구'),
        ('영등포구', '영등포구'),
        ('용산구', '용산구'),
        ('은평구', '은평구'),
        ('종로구', '종로구'),
        ('중구', '중구'),
        ('중랑구', '중랑구'),
    )

    WAY_CHOICES = WayChoices.choices
    title = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='posts')
    description = models.TextField(blank=True)
    address = models.CharField(max_length=50, choices=DISTRICT_CHOICES)
    way = models.CharField(max_length=10, choices=WAY_CHOICES, null=True)
    start_time = models.CharField(max_length=100, null=True)
    startpoint = models.CharField(max_length=50)
    endpoint = models.CharField(max_length=50)
    address_end = models.CharField(max_length=50, choices=DISTRICT_CHOICES, null=True)  # 도착구
    count = models.IntegerField(default=0)  # 0이상의 정수
    countcheck = models.IntegerField(default=0)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.title


class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)  # 게시글 삭제될 때 같이 삭제
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=200)  # 댓글 내용
    review = models.BooleanField(default=False)  # 리뷰유무
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

class Apply(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)  # 게시글 삭제될 때 같이 삭제
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    complete = models.BooleanField(default=False)


    def __str__(self):
        return self.user.name

    def save_apply(board, user):
        apply = Apply(board=board, user=user)
        apply.complete = True
        apply.save()
