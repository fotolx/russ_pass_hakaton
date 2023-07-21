from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    # path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('', AdsList.as_view()),
    path('ads/', AdsList.as_view(), name='ads_list'), 
    path('myads/', UserAdsList.as_view(), name='user_ads'), 
    path('replies/', RepliesList.as_view(), name='replies'), 
    path('replies/<int:pk>/accept/', ReplyAccept.as_view(), name='accept_reply'), 
    path('replies/<int:pk>/delete/', ReplyDelete.as_view(), name='delete_reply'), 
    path('ads/<int:pk>', AdDetails.as_view(), name='details'),
    path('add', AdsAdd.as_view(), name='add'), 
    path('ads/<int:pk>/reply', SendMessage.as_view(), name='send_message'),
    path('ads/<int:pk>/edit/', AdsEdit.as_view(), name='edit_ad'),
]