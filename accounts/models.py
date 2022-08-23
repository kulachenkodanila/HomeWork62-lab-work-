from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Profile(models.Model):
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True, verbose_name='Аватар')
    profile_git = models.URLField(null=True, blank=True, max_length=500, verbose_name='Ссылка на GitHub аккаунт')
    about_user = models.TextField(null=True, blank=True, verbose_name='О себе')
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь', related_name='profile')