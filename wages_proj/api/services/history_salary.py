from django import forms
from service_objects.services import Service

from database.models import Salary


class HistorySalaryService(Service):
    user_id = forms.IntegerField(required=True)

    def process(self):
        return Salary.objects.filter(user_id=self.cleaned_data.get('user_id')).order_by('-created_at')
