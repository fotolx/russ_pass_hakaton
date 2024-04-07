"""
URL configuration for ad_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from travels.views import * # AdsList #,CustomLoginView, ResetPasswordView, profile, ChangePasswordView
from django.contrib.auth import views as auth_views
from auth_users.forms import LoginForm, RegisterForm
from auth_users.views import CustomLoginView, ResetPasswordView, profile, ChangePasswordView, ChangePasswordView, CustomLoginView, ResetPasswordView, RegisterView 
# from .views import ChangePasswordView, CustomLoginView, ResetPasswordView, home, RegisterView 
from django.views.generic import TemplateView

urlpatterns = [
    # path('', AdsList.as_view()), 
    # path('auth/', include('auth_users.urls')),
    path('admin/', admin.site.urls),
    # path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
    #                                        authentication_form=LoginForm), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    # path('password-reset-confirm/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
    #      name='password_reset_confirm'),
    # path('password-reset-complete/',
    #      auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
    #      name='password_reset_complete'),
    # path('profile/', profile, name='users-profile'),
    # path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('', include('travels.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('profile/', profile, name='users-profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

    path('register/', RegisterView.as_view(), name='register'),
    # path('register/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='russpass/registration.html',
    #                                        authentication_form=RegisterForm), name='register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='russpass/authorization.html',
                                           authentication_form=LoginForm), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='flatpages/mainpage.html'), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('profile/', profile, name='users-profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

    # Static pages
    # path("", TemplateView.as_view(template_name="russpass/index.html"), name='main'),
    path("dashboard/", TemplateView.as_view(template_name="russpass/dashboard.html"), name='dashboard'),
    path("marshrut/", TemplateView.as_view(template_name="russpass/marshrut.html"), name='marshrut'),
    # path("park/", TemplateView.as_view(template_name="russpass/park.html"), name='park'),
    path("plan/", TemplateView.as_view(template_name="russpass/plan.html"), name='plan'),
    path("bonus/", TemplateView.as_view(template_name="russpass/bonus.html"), name='bonus'),
    path("constructor/", TemplateView.as_view(template_name="russpass/constructor.html"), name='constructor'),
    path("start/", TemplateView.as_view(template_name="russpass/start.html"), name='start'),
    # path("route_add/", TemplateView.as_view(template_name="russpass/dyn/route_add.html"), name='route_add'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
