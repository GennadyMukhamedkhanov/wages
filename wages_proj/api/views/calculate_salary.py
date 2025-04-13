from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.services.calculate_salary import CalculateSalaryService
from api.tasks import send_salary_message


class CalculateSalary(APIView):
    def post(self, request):
        salary = CalculateSalaryService.execute(request.data)
        salary_data = {
            'id': salary.id,
            'user_id': salary.user_id,
            'period_start': salary.period_start,
            'period_end': salary.period_end,
            'total_hours': salary.total_hours,
            'gross_salary': salary.gross_salary,
            'deductions': salary.deductions,
            'net_salary': salary.net_salary,

        }
        send_salary_message.delay(**salary_data)

        return Response({"salary_id": salary.id}, status=status.HTTP_201_CREATED)
