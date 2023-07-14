from django.urls import path
from . import views
from .views import comment_post_all, comment_edit


urlpatterns = [
    path('board/', views.board_list, name = 'board_list'),
    path('board/<int:pk>/', views.board_detail, name='board_detail'),
    path('board/post/', views.board_post, name='board_post'),
    path('board/<int:pk>/edit/', views.board_edit, name='board_edit'),
    path('board/done/', views.done_list, name='done_list'),
    path('board/done/<int:pk>/', views.board_done, name='board_done'),
    path('board/<int:pk>/delete/', views.board_delete, name='board_delete'),
    path('board/search', views.search, name='search'),
    #여기부터 댓글
    path('comment/post/<int:pk>/',comment_post_all, name="comment_post"),
    path('comment/delete/<int:pk>/<int:comment_pk>/',views.comment_delete,name="comment_delete"),
    path('comment/edit/<int:pk>/<int:comment_pk>/',comment_edit,name="comment_edit"),
    #path('review_commment/<int:pk>/<int:comment_pk>/',views.review_comment,name="review_comment"),
    #path('just_commment/<int:pk>/<int:comment_pk>/',views.review_comment,name="just_comment"),
    #path('review_commment_list/<int:pk>/',views.review_comment_list,name="review_comment_list"),

]