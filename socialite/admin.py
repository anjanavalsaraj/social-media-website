from django.contrib import admin
from  .models import User,Post,Home_page_post,user_profile,Comment,FriendRequest

# Register your models here.

admin.site.register(Home_page_post)

class PostAdmin(admin.ModelAdmin):
    # list_display = ('title','slug','image','content','content2','created_by')
    prepopulated_fields = {'slug': ('title',)}

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','dob','gender','mobile','photo','place','profession','company')


admin.site.register(user_profile,ProfileAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(FriendRequest)