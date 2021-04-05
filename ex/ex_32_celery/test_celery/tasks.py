from __future__ import absolute_import
from test_celery.celery import app
import time

# window 문제 #
import os
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
# ########## #

@app.task()
def longtime_add(x, y):
    print('long time task begins')
    # sleep 5 seconds
    time.sleep(5)
    print('long time task finished')
    return x + y