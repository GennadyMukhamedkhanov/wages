from django.db import models


class Salary(models.Model):
    user_id = models.IntegerField()  # Внешний ключ на пользователя (ID пользователя на другом сервере)
    period_start = models.DateField()  # Начало расчетного периода
    period_end = models.DateField()  # Конец расчетного периода
    total_hours = models.DecimalField(max_digits=10, decimal_places=2)  # Общее количество отработанных часов
    gross_salary = models.DecimalField(max_digits=10, decimal_places=2)  # Валовая заработная плата
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Удержания
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)  # Чистая заработная плата
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания записи

    def __str__(self):
        return f'Salary for User {self.user_id} from {self.period_start} to {self.period_end}'
