from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """тема, которую изучает пользоваель"""
    text = models.CharField(max_length=200, verbose_name='Название темы')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta():
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.text


class Entry(models.Model):
    """Записи, изученные пользователем"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = "Записи"

    def __str__(self):
        """возврат строки"""
        if len(self.text) > 50:
            return f'{self.text[0:50]}...'
        else:
            return self.text
