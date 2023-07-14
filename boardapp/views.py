from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from account.models import User
from .models import Board, Comment, Apply
from .forms import PostForm, AddressFilterForm, CommentForm


# Create your views here.



def board_list(request):
    address_filter = request.GET.get('address', '')  # 주소 필터링 값을 가져옴

    if address_filter:  # 주소 필터링 값이 있다면 해당 주소의 게시글만 필터링
        boards = Board.objects.filter(address=address_filter, complete=False)
    else:  # 주소 필터링 값이 없다면 모든 게시글 표시
        boards = Board.objects.filter(complete=False)

    address_choices = Board.DISTRICT_CHOICES  # 주소 선택지

    context = {
        'boards': boards,
        'address_choices': address_choices,
        'selected_address': address_filter,  # 선택한 주소를 템플릿으로 전달
    }

    return render(request, 'board/board_list.html', context)


def board_detail(request,pk):
    board = Board.objects.get(id=pk)
    return render(request, 'board/board_detail.html',{'board':board})

def board_post(request):
    if request.method == 'POST':
        print(request.POST)
        form = PostForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            board = form.save(commit=False)
            board.user = request.user

            print(board.user)
            board.save()
            return redirect('board_list')
    else:
        form =PostForm()
    return render(request, 'board/board_post.html',{'form':form})

def board_edit(request, pk):
    board = Board.objects.get(id=pk)
    if request.method == "POST":
        print(request.POST)
        form = PostForm(request.POST, instance=board)
        print(form.is_valid())
        if form.is_valid():
            board = form.save(commit=False)
            board.save()
            return redirect('board_list')
    else:
        form = PostForm(instance=board)
    return render(request, 'board/board_post.html',{'form': form})
#모집 완료
def done_list(request):
    dones = Board.objects.filter(complete=True)
    return render(request, 'board/done_list.html', {'dones': dones})

'''def board_done(request, pk):
    board = Board.objects.get(id=pk)



    Apply.save_apply(board, request.user)
    board.countcheck += 1
    if board.count == board.countcheck:
        board.complete = True
    board.save()
    apply = Apply.objects.get(request , id=board.pk)
    print(apply)
    return redirect('board_list')'''
def board_done(request, pk):
    board = get_object_or_404(Board, id=pk)
    apply = Apply.objects.filter(board=board, user=request.user).first()

    if apply is None:
        Apply.save_apply(board, request.user)
        board.countcheck += 1
        if board.count == board.countcheck:
            board.complete = True
        board.save()
        return redirect('board_list')
    else:
        messages.warning(request, '이미 신청하였습니다.')
        return redirect('board_detail', pk)


def board_delete(request, pk):
    board = Board.objects.get(id=pk)
    board.delete()
    return redirect('board_list')

def search(request):
    boards = Board.objects.filter(complete=False).order_by('-id')

    #boards = Board.objects.all().order_by('-id')

    q = request.POST.get('q', "")

    if q:
        boards = boards.filter(title__icontains=q)
        return render(request, 'board/search.html', {'boards': boards, 'q': q})

    else:
        return render(request, 'board/search.html')

#여기부터 댓글
#한번에 작성을 구현
def comment_post_all(request,pk):
    post = Board.objects.get(id=pk)
    if post.complete == True: #리뷰인 경우
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                content = form.cleaned_data['content']
                comment = Comment.objects.create(content=content, board=post, review = True)
                comment.user = request.user
                comment.save()
                return redirect('board_detail',pk)
        else:
            form = CommentForm()
        return render(request,'board_detail.html', {'form':form})
    else:
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                content = form.cleaned_data['content']
                comment = Comment.objects.create(content=content, board=post, review=False)
                comment.user = request.user
                comment.save()
                return redirect('board_detail', pk)
        else:
            form = CommentForm()
        return render(request, 'board_detail.html', {'form': form})

'''def comment_post(request,pk):
    post = Board.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            comment = Comment.objects.create(content=content, board=post)
            return redirect('board_detail',pk)
    else:
        form = CommentForm()
    return render(request,'board_detail.html', {'form':form})

def review_post(request, pk):
    dones = Board.objects.filter(complete=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            comment = Comment.objects.create(content=content, board=dones)
            return redirect('done_list', pk)'''



def comment_delete(request, pk, comment_pk):
    comment = Comment.objects.get(pk= comment_pk)
    comment.delete()
    return redirect('board_detail', pk)

def comment_edit(request,pk,comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    form=CommentForm(instance=comment)
    if request.method =='POST':
        edit_form = CommentForm(request.POST, instance=comment)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('board_detail', pk)

    return render(request, 'board/comment_edit.html', {'form':form})

'''def review_comment(request, pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.review = True
    comment.save()
    return redirect('board_detail')

def just_comment(request,pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.review = False
    comment.save()
    return redirect('board_detail')'''

def review_comment_list(request, pk, comment_pk):
    comments = Comment.objects.filter(review=False)
    return render(request, 'board_detail.html', {'comments':comments})


