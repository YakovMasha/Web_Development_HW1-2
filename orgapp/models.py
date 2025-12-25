from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField('Название', max_length=100, unique=True)
    description = models.TextField('Описание', blank=True)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ['name']

    def __str__(self):
        return self.name


class Position(models.Model):
    title = models.CharField('Должность', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['title']

    def __str__(self):
        return self.title


class Membership(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        verbose_name='Организация'
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,  # ← при удалении должности — поле станет NULL
        null=True,                   # ← разрешаем NULL
        blank=True,                  # ← разрешаем пустое значение в формах
        verbose_name='Должность'
    )
    joined_at = models.DateField('Дата вступления', auto_now_add=True)

    class Meta:
        verbose_name = 'Членство'
        verbose_name_plural = 'Членства'
        unique_together = ('user', 'organization')  # ← один пользователь — одна запись в одной организации
        ordering = ['organization', 'user']

    def __str__(self):
        pos = self.position.title if self.position else 'Сотрудник'
        return f"{self.user.username} → {self.organization.name} ({pos})"