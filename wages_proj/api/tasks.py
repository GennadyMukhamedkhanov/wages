from celery import shared_task, Celery

app = Celery('tasks', broker='pyamqp://rmuser:rmpassword@45.144.65.161:5672//')


@app.task(queue='message')
def send_salary_message(**kwargs):
    print('Ваполнение задачи send_salary_message!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
