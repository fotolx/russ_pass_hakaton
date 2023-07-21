from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse
from .models import Profile, Replies, Ads
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMultiAlternatives
from ad_site.settings import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_USE_SSL
from .management.commands.runapscheduler import weekly_mail
from datetime import date

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=Replies)
def mail_to_author(sender, instance, created, **kwargs):
    try:
        accepted = instance.accepted
        ad_id = instance.ad_id
        ad_header = instance.ad.header
        author_mail = instance.ad.author.username.email
        current_site = Site.objects.get_current()
        author_name = f'{instance.ad.author.username.first_name} {instance.ad.author.username.last_name}'
        replyed_user_name = f'{instance.user.first_name} {instance.user.last_name}'
        
        post_link = f"http://{current_site.name}{reverse('details', args=(ad_id,))}"
        if accepted: # Отклик принят
            header = f'Принят твой отклик на объявление "{ad_header}"'
            main_text = f'Пользователь {author_name} принял твой отклик.'
            hello_text = f'Здравствуй, {replyed_user_name}. Принят твой отклик на объявление!\n'
            author_mail = instance.user.email
        else: # Кто-то откликнулся на объявление
            replies_link = reverse('replies')
            header = f'Новый отклик на объявление "{ad_header}"'
            main_text = f'Пользователь {replyed_user_name} откликнулся на твое объявление <a href="{ post_link }">{ header }</a>.\nЗайди на свою <a href="{ replies_link }">страничку с откликами</a> и посмотри, какие еще есть.'
            hello_text = f'Здравствуй, {author_name}. Новый отклик на твоё объявление!\n'
            author_mail = instance.ad.author.username.email

        html_content = render_to_string('email/mail_to_author.html', {'header': header, 'main_text': main_text, 'hello_text': hello_text, 'post_link': post_link})
        msg = EmailMultiAlternatives(
        subject=f'{header}',
        body=hello_text+main_text,
        from_email=EMAIL_HOST_USER,
        to=[author_mail],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    except ObjectDoesNotExist:
        pass

@receiver(weekly_mail)
def weekly_mail(sender, **kwargs):
    current_site = Site.objects.get_current()
    site_link = f"http://{current_site.name}"
    print('Digest')
    current_site = Site.objects.get_current()
    weekly_ads = Ads.objects.filter(date_time__week=date.today().isocalendar()[1]-1)
    users_to_send = Profile.objects.filter()
    for each in users_to_send:
        if len(each.user.email):
            hello_text = f'Здравствуй, {each.user.first_name} {each.user.last_name}. Подборка объявлений за неделю!\n'
            header = 'Подборка объявлений за неделю'
            html_content = render_to_string('email/news_mail.html', 
                                            {'header': header, 'hello_text': hello_text, 'posts': weekly_ads, 'site_link': site_link})
            msg = EmailMultiAlternatives(
            subject=f'{header}',
            body=hello_text,
            from_email=EMAIL_HOST_USER,
            to=[each.user.email],
            )
            msg.attach_alternative(html_content, "text/html") # добавляем html
            msg.send()
    