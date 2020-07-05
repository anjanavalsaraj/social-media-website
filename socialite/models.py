from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Post(models.Model):
    title       =   models.CharField(max_length=100,null=True,blank=True)
    slug        =   models.SlugField(max_length=120,null=True,blank=True)
    image       =   models.ImageField(null=True,blank=True)
    content     =   models.TextField(default='',null=True,blank=True)

    content2    =   models.CharField(max_length=100,default='',null=True)

    created_by  =   models.ForeignKey(User,related_name='post_s',on_delete=models.CASCADE)
    likes       =   models.ManyToManyField(User, related_name='likes', blank=True)
    created_on  =   models.DateTimeField(auto_now_add=True)
    updated_on  =   models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id,self.slug])

    def total_likes(self):
        return self.likes.count()

@receiver(pre_save,sender=Post)
def pre_save_slug(sender,**kwargs):
    slug=slugify(kwargs['instance'].title)
    kwargs['instance'].slug=slug


    # def __str__(self):
    #     return self.created_by,"s post"

class Home_page_post(models.Model):
    post_created_by     =   models.ForeignKey(User,related_name='home_post',on_delete=models.CASCADE)
    post_body           =   models.CharField(max_length=100)
    post_created_on     =   models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Post by" , self.post_created_by

class user_profile(models.Model):

    GENDER_CHOICES=(
        ('male','Male'),
        ('female','Female'),
    )

    PLACE_CHOICES=(
        ('kerala','Kerala'),
        ('chennai','Chennai'),
        ('bangalore','Bangalore'),
        ('mysore','Mysore'),
        ('mumbai','Mumbai'),
        ('dubai','Dubai'),
        ('america','America'),
    )
    PROFESSION_CHOICES=(
        ('Software engineer','Software engineer'),
        ('Graphic designer','Graphic designer'),
        ('Content Writer','Content Writer'),
        ('Senior accountant','Senior accountant'),
        ('HR Manager','HR Manager'),
        ('Sales manager','Sales manager'),
        ('Nurse','Nurse'),
        ('Business development associate','Business development associate'),
        ('Project co-ordinator','Project co-ordinator'),
        ('Flight attendant','Flight attendant'),
        ('Seo analyst','Seo analyst'),
        ('Student','Student'),
    )
    COMPANY_CHOICES=(
        ('SBI','SBI'),
        ('Wipro','Wipro'),
        ('Accenture','Accenture'),
        ('Byjus','Byjus'),
        ('Max Innovations','Max Innovations'),
        ('HDFC','HDFC'),
        ('ABC Corporation','ABC Corporation'),
        ('Contracting plus','Contracting plus'),
        ('Techbyte technologies','Techbyte technologies'),
        ('Jet airways','Jet airways'),
        ('Infosys','Infosys'),
        ('Careplus hospital','Careplus hospital'),
    )

    user        =   models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')

    dob         =   models.DateField(null=True,blank=True)
    gender      =   models.CharField(choices=GENDER_CHOICES, max_length=128)
    mobile      =   models.CharField(max_length=12)
    photo       =   models.ImageField(null=True, blank=True)
    place       =   models.CharField(choices=PLACE_CHOICES,max_length=128)
    profession  =   models.CharField(choices=PROFESSION_CHOICES,max_length=128,null=True,blank=True)
    company     =   models.CharField(choices=COMPANY_CHOICES,max_length=128,null=True,blank=True)
    friends     =   models.ManyToManyField(User, blank=True, related_name='friends')

class FriendRequest(models.Model):
    from_user   =   models.ForeignKey(User,related_name='from_user',on_delete=models.CASCADE)
    to_user     =   models.ForeignKey(User,related_name='to_user',on_delete=models.CASCADE)

class Comment(models.Model):
    user        =   models.ForeignKey(User,on_delete=models.CASCADE)
    post        =   models.ForeignKey(Post,on_delete=models.CASCADE)
    content     =   models.TextField(max_length=200,default='')
    timestamp   =   models.DateTimeField(auto_now_add=True)