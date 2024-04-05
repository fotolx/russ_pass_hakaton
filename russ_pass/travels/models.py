from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from auth_users.models import Users

# Create your models here.
# class Users(models.Model):
#     username = models.OneToOneField(User, on_delete=models.CASCADE)
#     user_rating = models.IntegerField(default=0)
#     author = models.BooleanField(default=True)
#     subsribed_to_newsletter = models.BooleanField(default=False)
#     mail_confirmed = models.BooleanField(default=False)
#     banned = models.BooleanField(default=False)

#     def __str__(self):
#         return f'{self.username}'
    
#     def update_rating(self):
#         pass

# class Category(models.Model):
#     name = models.CharField(unique=True, max_length=255, null=False, verbose_name="Категория")
#     user = models.ManyToManyField(User, through = 'UsersSubscribed')
#     description = models.CharField(max_length=255)
#     hidden = models.BooleanField(default=False)

#     def __str__(self):
#         return f'{self.name}'

# class Ads(models.Model):
#     header = models.CharField(max_length=255, null=False, verbose_name="Заголовок")
#     main_text = models.TextField(verbose_name="Текст объявления")
#     author = models.ForeignKey(Users, null=False, on_delete = models.CASCADE, verbose_name="Автор")
#     date_time = models.DateTimeField(auto_now_add = True)
#     category = models.ManyToManyField(Category, through = 'AdsCategory', verbose_name="Категория")
#     end_up = models.DateTimeField(verbose_name="Окончание срока публикации")
#     moderated = models.BooleanField(default=False)
#     hidden = models.BooleanField(default=False)
#     blocked = models.BooleanField(default=False)

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

#     def preview(self):
#         return self.main_text[:20]+'...'
    
#     def __str__(self):
#         return f'{self.id} {self.header} [{self.author}]'
    
#     def get_absolute_url(self): 
#         return reverse('ads_list', kwargs={'id': self.id})

# class AdsCategory(models.Model):
#     ad = models.ForeignKey(Ads, on_delete = models.CASCADE, verbose_name="Объявление")
#     category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name="Категория")

# class UsersSubscribed(models.Model):
#     user = models.ForeignKey(User, on_delete = models.CASCADE)
#     category = models.ForeignKey(Category, on_delete = models.CASCADE)

#     def __str__(self):
#         return f'{self.user} is subscribed to category {self.category}'
    
# class Replies(models.Model): 
#     user = models.ForeignKey(User, on_delete = models.CASCADE)
#     ad = models.ForeignKey(Ads, on_delete = models.CASCADE, verbose_name="Объявление")
#     text = models.TextField(verbose_name="Текст")
#     date_time = models.DateTimeField(auto_now_add = True)
#     viewed = models.BooleanField(default=False)
#     accepted = models.BooleanField(default=False)

#     def replies_to_ads(user):
#         return Replies.objects.filter(ad__author=user.users)
#         pass

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     avatar = models.ImageField(default='default_userpic.png', upload_to='images/profile/')
#     bio = models.TextField()

#     def __str__(self):
#         return self.user.username
    
#     # resizing images
#     def save(self, *args, **kwargs):
#         super().save()
#         img = Image.open(self.avatar.path)
#         if img.height > 100 or img.width > 100:
#             new_img = (100, 100)
#             img.thumbnail(new_img)
#             img.save(self.avatar.path)



class Region(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'

class Transport(models.Model):
    # id = models.AutoField(primary_key=True)
    type = models.CharField(unique=True, max_length=100, verbose_name="Тип транспорта")
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='images/transport_icons/', blank=True)

    def __str__(self):
        return f'{self.type}'

class RouteType(models.Model):
    # id = models.AutoField(primary_key=True)
    type = models.CharField(unique=True, max_length=100, verbose_name="Тип маршрута")
    icon = models.ImageField(upload_to='images/route_icons/', blank=True)
    
    def __str__(self):
        return f'{self.type}'

class Tags(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='images/tag_icons/', blank=True)

    def __str__(self):
        return f'{self.name}'

class Route(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(unique=False, max_length=100, verbose_name="Название")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Регион")
    type = models.ForeignKey(RouteType, on_delete=models.CASCADE, verbose_name="Тип маршрута", blank=True, null=True)
    tags = models.ManyToManyField(Tags, through='RouteTags', blank=True, verbose_name="Теги")
    image = models.ImageField(default='blank_preview.png', upload_to='images/', blank=True, verbose_name="Изображение")
    preview_small = models.ImageField(default='blank_preview.png', upload_to='images/small/', blank=True, verbose_name="Превью маленькое")
    preview_big = models.ImageField(default='default_hero.png', upload_to='images/big/', blank=True, verbose_name="Превью большое")
    exp_points = models.IntegerField(default=0, null=True, verbose_name="Очки опыта")
    bonuses = models.IntegerField(default=0, verbose_name="Бонусы")
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Транспорт")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return f'{self.name}'

class RouteTags(models.Model):
    # id = models.AutoField(primary_key=True)
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tags, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.route_id.name+" - "+self.tag_id.name}'

# class Users(models.Model):
#     # id = models.AutoField(primary_key=True)
#     username = models.OneToOneField(User, on_delete=models.CASCADE)
#     FirstName = models.CharField(max_length=100)
#     LastName = models.CharField(max_length=100)
#     Reg_date = models.DateField()
#     Region = models.ForeignKey('Region', on_delete=models.CASCADE)
#     gender = models.CharField(max_length=10)
#     email = models.EmailField()
#     phone = models.CharField(max_length=15)
#     about = models.TextField()
#     avatar = models.ImageField(upload_to='avatars/')

# class Users(models.Model):
#     username = models.OneToOneField(User, on_delete=models.CASCADE)
#     user_rating = models.IntegerField(default=0)
#     author = models.BooleanField(default=True)
#     subsribed_to_newsletter = models.BooleanField(default=False)
#     mail_confirmed = models.BooleanField(default=False)
#     banned = models.BooleanField(default=False)

#     def __str__(self):
#         return f'{self.username}'
    
#     def update_rating(self):
#         pass


class Favourites(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="Пользователь")
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name="Маршрут")
    date_added = models.DateField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return f'{self.route_id.name+" - "+self.user}'

class CompletedRoutes(models.Model):
    # id = models.AutoField(primary_key=True)
    date_created = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    date_pass = models.DateField(blank=True, verbose_name="Дата прохождения")
    complete_percent = models.IntegerField(default=0, verbose_name="Процент завершения")
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name="Маршрут")
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="Пользователь")

class Point(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    geo = models.CharField(max_length=100, blank=True, verbose_name="Гео-точка")
    image = models.ImageField(upload_to='images/', blank=True, verbose_name="Изображение")
    type = models.CharField(max_length=100, blank=True, verbose_name="Тип точки")
    
    def __str__(self):
        return f'{self.name}'

class RoutePoints(models.Model):
    # id = models.AutoField(primary_key=True)
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
    point_id = models.ForeignKey(Point, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.route_id.name+" - "+self.point_id.name}'

class Selection(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='images/', blank=True, verbose_name="Изображение")

    def __str__(self):
        return f'{self.name}'

class SelectionContent(models.Model):
    # id = models.AutoField(primary_key=True)
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
    selection_id = models.ForeignKey(Selection, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.route_id.name+" - "+self.selection_id.name}'

class Event(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    date = models.DateField(auto_now_add=True, verbose_name="Дата")
    time = models.TimeField(auto_now_add=True, verbose_name="Время")
    image = models.ImageField(upload_to='images/', blank=True, verbose_name="Изображение")
    start_time = models.TimeField(blank=True, verbose_name="Время начала")
    end_Time = models.TimeField(blank=True, verbose_name="Время окончания")

    def __str__(self):
        return f'{self.name}'

class Options(models.Model):
    # id = models.AutoField(primary_key=True)
    type = models.CharField(unique=True, max_length=100, verbose_name="Тип")
    name = models.CharField(max_length=100, blank=True, verbose_name="Название")
    icon = models.ImageField(upload_to='images/options_icons/', blank=True, verbose_name="Иконка")

    def __str__(self):
        return f'{self.type+" "+self.name}'

class FoodTypes(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100, verbose_name="Название")

    def __str__(self):
        return f'{self.name}'

class Food(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Название")
    type = models.ForeignKey(FoodTypes, on_delete=models.CASCADE, verbose_name="Тип питания")
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, verbose_name="Стоимость")
    rating = models.FloatField(default=4.5, verbose_name="Рейтинг")
    options = models.ManyToManyField(Options, through='FoodOptions', verbose_name="Опции")
    image_preview = models.ImageField(upload_to='images/small/', blank=True, verbose_name="Превью")
    image_big = models.ImageField(upload_to='images/big/', blank=True, verbose_name="Большое изображение")

    def __str__(self):
        return f'{self.name}'

class FoodOptions(models.Model):
    # id = models.AutoField(primary_key=True)
    options_id = models.ForeignKey(Options, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.options_id.type+" - "+self.food_id.name}'

class AccommodationType(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'

class Accommodation(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Название")
    type = models.ForeignKey(AccommodationType, on_delete=models.CASCADE, verbose_name="Тип жилья")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, verbose_name="Стоимость")
    rating = models.FloatField(blank=True, verbose_name="Рейтинг")
    description = models.TextField(blank=True, verbose_name="Описание")
    image_preview = models.ImageField(upload_to='images/small/', blank=True, verbose_name="Превью")
    image_big = models.ImageField(upload_to='images/big/', blank=True, verbose_name="Большое изображение")
    options = models.ManyToManyField(Options, through='AccomodationOptions', verbose_name="Опции")
    address = models.TextField(blank=True, verbose_name="Адрес")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Регион")

    def __str__(self):
        return f'{self.name}'

class AccomodationOptions(models.Model):
    # id = models.AutoField(primary_key=True)
    options_id = models.ForeignKey(Options, on_delete=models.CASCADE)
    accomodation_id = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='images/accomodation_icons/', blank=True, verbose_name="Иконка")

    def __str__(self):
        return f'{self.options_id.type+" - "+self.accomodation_id.name}'

class Excursion(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Название")
    date = models.DateField(auto_now_add=True, verbose_name="Дата")
    guide = models.CharField(max_length=100, blank=True, verbose_name="Гид")
    description = models.TextField(blank=True, verbose_name="Описание")
    date_start = models.DateField(blank=True, verbose_name="Дата начала")
    date_end = models.DateField(blank=True, verbose_name="Дата окончания")
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, verbose_name="Стоимость")
    rating = models.FloatField(blank=True, verbose_name="Рейтинг")
    image_preview = models.ImageField(upload_to='images/small/', blank=True, verbose_name="Превью")
    image_big = models.ImageField(upload_to='images/big/', blank=True, verbose_name="Большое изображение")

    def __str__(self):
        return f'{self.name}'
    
class Todo_list(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="Пользователь")
    name = models.CharField(max_length=100, verbose_name="Дело")
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.name+" "+self.name}'
    
class Stuff_list(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="Пользователь")
    name = models.CharField(max_length=100, verbose_name="Вещь в дорогу")
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.name+" "+self.name}'