from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView
from .models import *
from django.contrib import messages
from django.views import View
from .forms import *
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .filters import ReplyFilter


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваш профиль успешно обновлен')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})


def home(request):
    return render(request, 'flatpages/mainpage.html')

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            Users.objects.create(username=User.objects.get(username=username))
            messages.success(request, f'Аккаунт создан для {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})

# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Ваш пароль успешно изменен"
    success_url = reverse_lazy('users-home')
 
# Create your views here.
class AdsList(ListView):
    model = Ads
    context_object_name = 'ads'
    template_name = 'ads_list.html'
    pass

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['page_header'] = "Все объявления"
        return context

class UserAdsList(LoginRequiredMixin, ListView):
    model = Ads
    context_object_name = 'ads'
    template_name = 'ads_list.html'
    queryset = Ads.objects.order_by('-id')
    pass

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['page_header'] = "Мои объявления"
        return context
    
    def get_queryset(self):
            return Ads.objects.filter(author=self.request.user.users)

class AdsAdd(LoginRequiredMixin, CreateView):
    model = Ads
    template_name = 'ads_add.html'
    context_object_name = 'ads'
    queryset = Ads.objects.order_by('-id')
    # paginate_by = 10
    fields = '__all__'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['form']= AdForm()
        context['categories'] = Category.objects.all()
        context['name'] = self.request.user.username 
        context['last_name'] = self.request.user.last_name
        context['first_name'] = self.request.user.first_name
        return context
    
    def post(self, request, *args, **kwargs):
        # берём значения для новой публикации из POST-запроса отправленного на сервер
        header = request.POST['header']
        main_text = request.POST['main_text']
        author = request.user.id
        category = request.POST['category']
        end_up = request.POST['end_up']
        ad = Ads(author=Users.objects.get(username=author), header=header, 
                 main_text=main_text, end_up=end_up)          

        ad.save()                                  # и сохраняем
        ad.category.set(category)                  # Добавляем категорию
        ad.save()                                  # и сохраняем
        messages.success(request, f'Объявление успешно добавлено')
        return super().get(request, *args, **kwargs) # отправляем пользователя обратно на GET-запрос.


class AdsEdit(LoginRequiredMixin, UpdateView):
    template_name = 'ads_edit.html'
    form_class = AdForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Ads.objects.get(pk=id)

class AdDetails(DetailView):
    template_name = 'ad_details.html'
    queryset = Ads.objects.all()
    pass

class SendMessage(CreateView):
    model = Replies
    queryset = Replies.objects.all()
    template_name = 'reply.html'
    fields = '__all__'
    context_object_name = 'reply_to'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ad_pk = context['view'].kwargs['pk']
        context['ads'] = Ads.objects.get(id=ad_pk)
        return context

    def post(self, request, *args, **kwargs):
        user = request.user
        ad = Ads.objects.get(id=kwargs['pk'])
        text = request.POST['text']
        reply = Replies(user = user, ad = ad, text = text)
        reply.save()
        messages.success(request, f'Сообщение успешно отправлено')
        return HttpResponseRedirect(reverse('details', kwargs={'pk': ad.id}))
    

class RepliesList(LoginRequiredMixin, ListView):
    model = Replies
    context_object_name = 'replies'
    template_name = 'view_replies.html'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context = {'form': FilterReplyForm({'ad_author': self.request.user.users}), 'ad_author': self.request.user.users}
        context['page_header'] = "Отклики на мои объявления"
        context['user_ads'] = set(map(lambda i: (i['ad_id']), Replies.objects.filter(ad__author=self.request.user.users).values('ad_id')))
        context['filter'] = ReplyFilter(self.request.GET, queryset=self.get_queryset().filter(ad__author=self.request.user.users))
        return context
    
class ReplyDelete(LoginRequiredMixin, DeleteView):
    template_name = 'reply_delete.html'
    model = Replies
    success_url = reverse_lazy('replies')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, f'Отклик удален')
        return super(ReplyDelete, self).delete(request, *args, **kwargs)

class ReplyAccept(LoginRequiredMixin, ListView):
    model = Replies
    context_object_name = 'replies'
    template_name = 'view_replies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get(self, request, *args, **kwargs):
        reply = Replies.objects.get(pk=self.kwargs.get('pk'))
        reply.accepted = True
        reply.save()
        messages.success(request, f'Отклик принят')
        return redirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse('replies')