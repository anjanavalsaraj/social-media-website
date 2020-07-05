from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .forms import *
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def base(request):
    return render(request,'base.html')

def user_register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user=form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user_profile.objects.create(user=new_user)
            messages.success(request,"User has been created successfully.Login to continue.")
            return HttpResponseRedirect(reverse('user_login'))
    else:
        form=UserRegistrationForm()
        context={
            'form':form
        }
        return render(request,'register.html',context)

def user_login(request):
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return redirect('/')
                else:
                    return HttpResponse("User inactive")
            else:
                return HttpResponse('User dosent exist')
    else:
        form=UserLoginForm()
        context={
            'login_form':form
        }
        return render(request,'login.html',context)

def user_logout(request):
    logout(request)
    return redirect('/user_login/')

def home_page(request):
    if request.method=='POST':
        form=Home_page_post_form(request.POST or None,files=request.FILES)

        if form.is_valid():
            home_page_post=form.save(commit=False)

            home_page_post.created_by=request.user

            home_page_post.save()

            return redirect('/')
    else:

        prof=user_profile.objects.all()
        post_list=Post.objects.all().order_by('-created_on')
        form=Home_page_post_form()
        # userz=User.objects.all()

        query=request.GET.get('q')
        if query:
            post_list=Post.objects.filter(
                Q(created_by__username=query)|
                Q(title__icontains=query)|
                Q(created_by__first_name=query)|
                Q(created_by__last_name=query)|
                Q(content__icontains=query)|
                Q(content2__icontains=query)
            )




        context={
            'prof':prof,
            'post_list':post_list,
            'form':form,
            # 'users':userz,

        }
        return render(request,'home.html',context)

def post_create(request):
    if request.method=='POST':
        form=PostCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.created_by=request.user
            post.save()
            messages.success(request,"Post created succesfully.")
            return redirect('/')
    else:
        form=PostCreateForm()
        context={
            'form':form
        }
        return render(request,'create_post.html',context)


def edit_profile(request):
    # profile = user_profile(user=request.user)

    if request.method=='POST':
        user_form=User_edit_form(data=request.POST or None,instance=request.user)
        profile_form=Profile_edit_form(data=request.POST or None,instance=request.user.profile,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,"Profile has been updated successfully.")
            return redirect('/')
    else:
        user_form=User_edit_form(instance=request.user)
        profile_form=Profile_edit_form(instance=request.user.profile)
        context={
            'user_form':user_form,
            'profile_form':profile_form,
        }
        return render(request,'edit_profile.html',context)


def profile_view(request,id):
    profile=user_profile.objects.get(id=id)
    friends=profile.friends.all()
    # friend_request=FriendRequest.objects.filter(to_user=request.user)

    posts=Post.objects.filter(created_by_id=profile.user).order_by('-image')
    context={
        'profile':profile,
        'posts':posts,
        'friends':friends

    }
    return render(request,'user_profile.html',context)

def post_detail(request,id,slug):
    post=Post.objects.get(id=id)
    comments=Comment.objects.filter(post=post)
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    if request.method=='POST':
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            content=request.POST.get('content')
            comment=Comment.objects.create(user=request.user,content=content,post=post)
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form=CommentForm()

    context={
        'comment_form':comment_form,
        'comments':comments,
        'post':post,
        'is_liked':is_liked,
        'total_likes':post.total_likes()
    }
    return render(request,'post_detail.html',context)

def like_post(request):
    post=Post.objects.get(id=request.POST.get('post_id'))
    is_liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked=False
        return HttpResponseRedirect(post.get_absolute_url())
    else:
        is_liked=True
        post.likes.add(request.user)
        return HttpResponseRedirect(post.get_absolute_url())

def send_request(request,id):
    from_user=request.user
    to_user=User.objects.get(id=id)
    friend_request=FriendRequest.objects.get_or_create(from_user=from_user,to_user=to_user)
    return redirect('/')

def accept_request(request,id):

   
    friend_request=FriendRequest.objects.get(id=id)
    user1=request.user
    user2=friend_request.from_user
    user1.profile.friends.add(user2)
    user2.profile.friends.add(user1)
    friend_request.delete()
    return HttpResponseRedirect(reverse('friend_request'))

def friend_request_view(request):
    friend_request = FriendRequest.objects.filter(to_user=request.user)

    context={
        'friend_request':friend_request
    }
    return render(request,'friend_request.html',context)

def friends_list(request,id):
    profile=user_profile.objects.get(id=id)
    friends=profile.friends.all()
    context={
        'friends':friends,
        'profile':profile
    }
    return render(request,'friends_list.html',context)
