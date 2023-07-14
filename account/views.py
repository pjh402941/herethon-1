from django.contrib.auth import authenticate, login

from boardapp.models import Board
from .models import *
from .forms import UserForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def signup(request):
    if request.method == "POST":
        print(request.POST)
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            account = form.save(commit=False)
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, email=email, password=raw_password)
            if user is not None:
                login(request, user)
            account.save()
            return redirect('account:login')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def my_page(request, pk):
    user = get_object_or_404(User, pk=pk)
    user_posts = user.posts.all()
    board = get_object_or_404(Board, pk=pk)
    context = {
        'user': user,
        'user_posts': user_posts,
        'board':board
    }
    return render(request, "my_page.html", context)

@login_required
def profile_page(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = board.user
    user_posts = user.posts.all()
    context = {
        'user': user,
        'user_posts' : user_posts
    }
    return render(request, "profile_page.html", context)

@login_required
def my_page_update(request, pk) :
    user = User.object.get(id=pk)
    if request.method == 'POST':
        print(request.POST)
        form = UserChangeForm(request.POST, request.FILES, instance=user)
        print(form.is_valid())
        if form.is_valid():
            if request.POST.get('school_photo') == '' :
                user.is_active = True
            else :
                user.is_active = False
            form.save()
            return redirect('board_list')
    else:
        form = UserChangeForm(instance=user)
    return render(request, "my_page_update.html", {'form': form})
@login_required
def admin_page (request) :
    users = User.object.all()

    return render(request, "admin_page.html", {"users": users})

@login_required
def admin_accept (request, pk) :
    users = User.object.all()
    user = get_object_or_404(User, id=pk)
    user.is_active = True
    user.save()
    return render(request, "admin_page.html", {"users": users})

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.object.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = '[Ando] 비밀번호 재설정'
                    email_template_name = "password_reset_email.txt"
                    c = {
                        "email": user.email,
                        # local: '127.0.0.1:8000', prod: 'givwang.herokuapp.com'
                        'domain': settings.HOSTNAME,
                        'site_name': 'ando',
                        # MTE4
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        # Return a token that can be used once to do a password reset for the given user.
                        'token': default_token_generator.make_token(user),
                        # local: http, prod: https
                        'protocol': settings.PROTOCOL,
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'jiyeon011004@gmail.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("done/")
    password_reset_form = PasswordResetForm()
    return render(
        request=request,
        template_name='password_reset.html',
        context={'password_reset_form': password_reset_form})
