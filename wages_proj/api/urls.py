from django.urls import path

from api.views.calculate_salary import CalculateSalary
from api.views.history_salary import HistorySalary

urlpatterns = [

    # Расчет заработной платы
    path('salary/calculate/', CalculateSalary.as_view(), name='salary_calculate'),
    path('salary/history/<int:id>/', HistorySalary.as_view(), name='salary_history'),
]