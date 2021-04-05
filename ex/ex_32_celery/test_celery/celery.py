from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery',
             broker='amqp://abc:abc@192.168.0.51/',
             backend='rpc://',
             include=['test_celery.tasks'])

# 1. test_celery 상위 디렉토리에서 실행
# celery -A test_celery worker --loglevel=info

# 2. 다른 콘솔에서 run_tasks.py 실행
# test_celery 상위 디렉토리에서 실행
# celery 콘솔에서 worker가 작업을 받음
# python -m test_celery.run_tasks

# 3. Monitor Celery in Real Time
# pip install flower
# test_celery 상위 디렉토리에서 실행
# celery -A test_celery flower
# http://localhost:5555 에서 확인