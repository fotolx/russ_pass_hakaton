from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

urlpatterns = [
    path("route_add/", RouteAdd.as_view(template_name="russpass/dyn/route_add.html"), name='route_add'),
    # path('dyn/', dyn_home, name='dyn_home'),

    # path('register/', RegisterView.as_view(), name='users-register'),
    # path("dashboard/", TemplateView.as_view(template_name="russpass/dashboard.html"), name='dashboard'),
    # path("marshrut/", TemplateView.as_view(template_name="russpass/marshrut.html"), name='marshrut'),
    # path("park/", TemplateView.as_view(template_name="russpass/park.html"), name='park'),
    
    path('park/<int:pk>', ParkDetails.as_view(template_name='russpass/park.html'), name='park'),
    path('', RoutesList.as_view(template_name="russpass/index.html"), name='main'), 
    path('dyn/marshrut/', RoutesList.as_view(template_name="russpass/dyn/marshrut.html"), name='dyn_marshrut'), 
]