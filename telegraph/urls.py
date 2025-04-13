from django.urls import path

from . import views


urlpatterns = [
    path('', views.create_post, name='create_post'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('edit/<uuid:edit_token>/', views.edit_post, name='edit_post'),
    path('post-list/', views.post_list, name='post_list'),
    path('post/<slug:slug>/delete/', views.delete_post, name='delete_post'),
]
