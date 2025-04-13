from functools import lru_cache
from decimal import Decimal

from django import forms
from rest_framework.exceptions import NotFound
from service_objects.services import Service

from database.models import WorkTime, Salary


class CalculateSalaryService(Service):
    user_id = forms.IntegerField(required=True)
    period_start = forms.DateField(required=True)
    period_end = forms.DateField(required=True)

    def process(self):
        return self.saving_data

    @property
    def saving_data(self):
        # Расчет заработной платы
        hourly_rate = 20  # Здесь можно получить ставку с другого сервиса
        gross_salary = self.total_hours() * hourly_rate
        deductions = gross_salary * Decimal(0.15)  # Пример удержаний
        net_salary = gross_salary - deductions

        # Сохранение результата в базе данных
        salary = Salary.objects.create(
            user_id=self.cleaned_data.get('user_id'),
            period_start=self.cleaned_data.get('period_start'),
            period_end=self.cleaned_data.get('period_end'),
            total_hours=self.total_hours(),
            gross_salary=gross_salary,
            deductions=deductions,
            net_salary=net_salary
        )
        return salary

    def work_time_records(self):
        list_work_time = WorkTime.objects.filter(
            user_id=self.cleaned_data.get('user_id'),
            date__range=[self.cleaned_data.get('period_start'), self.cleaned_data.get('period_end')]
        )
        if not list_work_time.exists():
            raise NotFound('Отработанных часов у данного пользователя не найдено')
        return list_work_time

    @lru_cache
    def total_hours(self):
        return sum(record.hours_worked for record in self.work_time_records())
