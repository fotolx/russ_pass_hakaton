from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# from travels.models import Region

# Create your models here.
class Users(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    reg_date = models.DateField(auto_now=True)
    # Region = models.ForeignKey(Region, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    # user_rating = models.IntegerField(default=0)
    # author = models.BooleanField(default=True)
    # subsribed_to_newsletter = models.BooleanField(default=False)
    # mail_confirmed = models.BooleanField(default=False)
    banned = models.BooleanField(default=False)
    # USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def update_rating(self):
        pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    avatar = models.ImageField(default='account.png', upload_to='images/profile/')
    about = models.TextField(default='',blank=True)

    def __str__(self):
        return self.user
    
    # resizing images
    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.avatar.path)
        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
