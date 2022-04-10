from django.db import models


class Topic(models.Model):
    """тема, которую изучает пользоваель"""
    text = models.CharField(max_length=200, verbose_name='Название темы')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

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
        return f'{self.text[0:50]}...'