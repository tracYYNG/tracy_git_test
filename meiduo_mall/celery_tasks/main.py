


import os
from celery import Celery

# 1.为celery的运行，配置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meiduo_mall.settings')

# 2.创建实力对象
app = Celery('celery_tasks')

# 3.设置中间人broker -> config.py
app.config_from_object('celery_tasks.config')

# 4.自动检测指定包的任务
app.autodiscover_tasks(['celery_tasks.sms'])