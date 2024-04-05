from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

urlpatterns = [
    path("route_add/", RouteAdd.as_view(template_name="russpass/dyn/route_add.html"), name='route_add'),
    path('dyn/', dyn_home, name='dyn_home'),

    # path('register/', RegisterView.as_view(), name='users-register'),
    # path('', AdsList.as_view(), name='main'),
    # path("dashboard/", TemplateView.as_view(template_name="russpass/dashboard.html"), name='dashboard'),
    # path("marshrut/", TemplateView.as_view(template_name="russpass/marshrut.html"), name='marshrut'),
    # path("park/", TemplateView.as_view(template_name="russpass/park.html"), name='park'),
    # path('ads/', AdsList.as_view(), name='ads_list'), 
    # path('myads/', UserAdsList.as_view(), name='user_ads'), 
    # path('replies/', RepliesList.as_view(), name='replies'), 
    # path('replies/<int:pk>/accept/', ReplyAccept.as_view(), name='accept_reply'), 
    # path('replies/<int:pk>/delete/', ReplyDelete.as_view(), name='delete_reply'), 
    path('dyn/park/<int:pk>', ParkDetails.as_view(), name='park_details'),
    # path('add', AdsAdd.as_view(), name='add'), 
    # path('ads/<int:pk>/reply', SendMessage.as_view(), name='send_message'),
    # path('ads/<int:pk>/edit/', AdsEdit.as_view(), name='edit_ad'),
]