from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='review-list'),    
    path('film/<int:film_id>/review/new/', views.review_create, name='review-create'),
    path('review/<int:pk>/', views.review_detail, name='review-detail'),
    # path('review/<int:pk>/edit/', views.review_edit, name='review-edit'),
    # path('review/<int:pk>/delete/', views.review_delete, name='review-delete'),
    # path('review/<int:pk>/like/', views.review_like, name='review-like'),
    # path('comment/<int:pk>/create/', views.comment_create, name='comment-create'),
    path('films/', views.FilmListView.as_view(), name='film-list'),
    # path('film/<int:film_id>/review/create/', views.review_create, name='review-create'),
    # path('comment/<int:pk>/delete/', views.comment_delete, name='comment-delete'),
]