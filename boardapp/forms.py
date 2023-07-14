import this

from django import forms
from django.contrib.auth import get_user_model
from django.http import request

from .models import Board, Comment
from account.models import User


class PostForm(forms.ModelForm): # 게시글 작성용 폼

    title = forms.CharField(label='제목')
    description = forms.CharField(label='설명')
    address = forms.CharField(label='출발구', widget=forms.Select(choices=Board.DISTRICT_CHOICES))
    startpoint = forms.CharField(label='출발지')
    endpoint = forms.CharField(label='도착지')
    address_end = forms.CharField(label='도착구', widget=forms.Select(choices=Board.DISTRICT_CHOICES))
    start_time = forms.CharField(label='출발 시각')
    count = forms.IntegerField(label='모집인원')  # 0이상의 정수
    way = forms.CharField(label='이동방식', widget=forms.Select(choices=Board.WAY_CHOICES))

    def save(self, commit=True):
        board = super().save(commit=False)
        if self.request is not None:
            board.user = self.request.user  # 현재 로그인한 사용자를 할당
        if commit:
            board.save()
        return board

    class Meta:
        model = Board
        fields = ['title', 'description', 'address', 'start_time', 'startpoint','address_end', 'endpoint', 'count', 'way']
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.request = kwargs.pop('request', None)  # request 객체를 인스턴스 변수로 저장
        self.fields['address_end'].widget = forms.Select(choices=Board.DISTRICT_CHOICES)
        self.fields['address'].widget = forms.Select(choices=Board.DISTRICT_CHOICES)
        self.fields['way'].widget = forms.Select(choices=Board.WAY_CHOICES)


class AddressFilterForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['address']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget = forms.Select(choices=Board.DISTRICT_CHOICES)

class CommentForm(forms.ModelForm): #댓글 작성용 폼

    #content = forms.CharField(label='댓글')
    #review = forms.BooleanField(label='리뷰')

    class Meta:
        model = Comment
        fields = ['content']

