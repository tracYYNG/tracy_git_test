from celery_tasks.main import app
from django.core.mail import send_mail

@app.task
def celery_send_email(send_message):
    send_mail(
            subject='主题',
            message='',
            from_email='tracy<tracyshenzl@163.com>',
            recipient_list=['582974285@qq.com'],
            html_message=send_message
        )