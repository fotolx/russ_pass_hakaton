from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'userssubscribed', '_users', )
#     list_filter = ('name',)

#     @admin.display(description='Users list',)
#     def	_users(self, row):
#         return ', '.join([x.username for x in row.user.all()])

#     @admin.display(description='Subscribers count',)
#     def userssubscribed(self, row):
#         return f'{row.userssubscribed_set.all().count()}' 
    
# class ProfileAdmin(admin.ModelAdmin):
#     # fields_admin = Profile._meta.get_fields()
#     # list_display = [field.name for field in Profile._meta.get_fields()]
#     list_display = ('id', 'fio', 'user', 'avatar', 'bio',)
#     list_filter = ('avatar', 'bio',)

#     def fio(self, row):
#         return f'{row.user.first_name} {row.user.last_name}'

# class UsersSubscribedAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in UsersSubscribed._meta.get_fields()]
#     list_filter = ('user', 'category',)
    
# Register your models here.
# admin.site.register(Category) #, CategoryAdmin)
# admin.site.register(Profile) #, ProfileAdmin)
# admin.site.register(UsersSubscribed) #, UsersSubscribedAdmin)
# admin.site.register(Users)
# admin.site.register(Ads)
# admin.site.register(AdsCategory)
# admin.site.register(Replies)

class RouteAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

# admin.site.register(Post, PostAdmin)

admin.site.register(Region)
admin.site.register(Transport)
admin.site.register(RouteType)
admin.site.register(Tags)
admin.site.register(RouteTags)
admin.site.register(Route, RouteAdmin)
# admin.site.register(Users)
admin.site.register(Favourites)
admin.site.register(CompletedRoutes)
admin.site.register(Point)
admin.site.register(RoutePoints)
admin.site.register(Selection)
admin.site.register(SelectionContent)
admin.site.register(Event)
admin.site.register(FoodTypes)
admin.site.register(Food)
admin.site.register(AccommodationType)
admin.site.register(Options)
admin.site.register(Accommodation)
admin.site.register(AccomodationOptions)
admin.site.register(Excursion)
admin.site.register(Level)