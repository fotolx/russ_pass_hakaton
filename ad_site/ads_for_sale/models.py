from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

# Create your models here.
class Users(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rating = models.IntegerField(default=0)
    author = models.BooleanField(default=True)
    subsribed_to_newsletter = models.BooleanField(default=False)
    mail_confirmed = models.BooleanField(default=False)
    banned = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username}'
    
    def update_rating(self):
        pass

class Category(models.Model):
    name = models.CharField(unique=True, max_length=255, null=False, verbose_name="Категория")
    user = models.ManyToManyField(User, through = 'UsersSubscribed')
    description = models.CharField(max_length=255)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

class Ads(models.Model):
    header = models.CharField(max_length=255, null=False, verbose_name="Заголовок")
    main_text = models.TextField(verbose_name="Текст объявления")
    author = models.ForeignKey(Users, null=False, on_delete = models.CASCADE, verbose_name="Автор")
    date_time = models.DateTimeField(auto_now_add = True)
    category = models.ManyToManyField(Category, through = 'AdsCategory', verbose_name="Категория")
    end_up = models.DateTimeField(verbose_name="Окончание срока публикации")
    moderated = models.BooleanField(default=False)
    hidden = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def preview(self):
        return self.main_text[:20]+'...'
    
    def __str__(self):
        return f'{self.id} {self.header} [{self.author}]'
    
    def get_absolute_url(self): 
        return reverse('ads_list', kwargs={'id': self.id})

class AdsCategory(models.Model):
    ad = models.ForeignKey(Ads, on_delete = models.CASCADE, verbose_name="Объявление")
    category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name="Категория")

class UsersSubscribed(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.user} is subscribed to category {self.category}'
    
class Replies(models.Model): 
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    ad = models.ForeignKey(Ads, on_delete = models.CASCADE, verbose_name="Объявление")
    text = models.TextField(verbose_name="Текст")
    date_time = models.DateTimeField(auto_now_add = True)
    viewed = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)

    def replies_to_ads(user):
        return Replies.objects.filter(ad__author=user.users)
        pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default_userpic.png', upload_to='images/profile/')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
    
    # resizing images
    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.avatar.path)
        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
