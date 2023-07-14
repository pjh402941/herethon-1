from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    # path('', views.main, name='main'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('my_page/<int:pk>', views.my_page, name='my_page'),
    path('profile_page/<int:pk>', views.profile_page, name="profile_page"),
    path('my_page/update/<int:pk>', views.my_page_update, name="my_page_update"),
    path('password_reset/', views.password_reset_request, name="password_reset"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
