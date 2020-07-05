from django.urls import path
from . import views

urlpatterns=[
    path('',views.home_page,name='home_page'),
    path('register/',views.user_register,name='user_register'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('create_post/',views.post_create,name='create_post'),
    path('profile/<int:id>/',views.profile_view,name='profile_view'),
    path('<int:id>/<slug:slug>',views.post_detail,name='post_detail'),
    path('like/',views.like_post,name='like_post'),
    path('add_friend/<int:id>/',views.send_request,name='add_friend'),
    path('accept/<int:id>/',views.accept_request,name='accept_request'),
    path('friend_request/',views.friend_request_view,name='friend_request'),
    path('friends/<int:id>/',views.friends_list,name='friends')
    # path('search/',views.search_user,name='search')


]