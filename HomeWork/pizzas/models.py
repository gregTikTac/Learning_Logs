from django.db import models


class Pizza(models.Model):
    pizza_name = models.CharField(max_length=50, verbose_name="Название Пиццы")

    class Meta():
        verbose_name_plural = 'Пицца'

    def __str__(self):
        return self.pizza_name


class Toppings(models.Model):
    pizza_name = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topings = models.TextField(verbose_name='Начинка для Пиццы')

    class Meta():
        verbose_name_plural = 'Начинка'

    def __str__(self):
        return self.topings
