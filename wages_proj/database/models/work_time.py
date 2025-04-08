from django.db import models


class WorkTime(models.Model):
    user_id = models.IntegerField()  # Внешний ключ на пользователя (ID пользователя на другом сервере)
    date = models.DateField()  # Дата рабочего дня
    hours_worked = models.DecimalField(max_digits=10, decimal_places=2)  # Количество отработанных часов

    def __str__(self):
        return f'WorkTime for User {self.user_id} on {self.date}'
