from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import validate_username


class User(AbstractUser):
    username = models.CharField(
        'Логин', max_length=150, unique=True, validators=(validate_username,)
    )
    email = models.EmailField(
        'Почта', max_length=254, unique=True
    )
    first_name = models.CharField(
        'Имя', max_length=150
    )
    last_name = models.CharField(
        'Фамилия', max_length=150
    )
    password = models.CharField(
        'Пароль', max_length=150
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [models.UniqueConstraint(
            fields=['username', 'email'], name='unigue_together')
        ]

    def __str__(self):
        return self.username


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор публикации'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [models.UniqueConstraint(
            fields=['user', 'author'], name='unigue_follow')
        ]

    def __str__(self):
        return f'{self.user} подписан на {self.author}'
