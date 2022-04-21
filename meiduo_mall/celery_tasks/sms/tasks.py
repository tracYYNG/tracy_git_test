from celery_tasks.main import app

@app.task
def celery_send_sms_code(sms_code):
    print('celery_send:' + sms_code)