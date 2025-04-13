from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.history import HistorySalarySerializer
from api.services.history_salary import HistorySalaryService


class HistorySalary(APIView):
    def get(self, request, **kwargs):
        historys = HistorySalaryService.execute({'user_id': kwargs['id']})
        serializer = HistorySalarySerializer(historys, many=True).data

        return Response(serializer, status=status.HTTP_200_OK)
