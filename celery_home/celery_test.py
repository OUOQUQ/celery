from celery import Celery
from celery.result import AsyncResult


app = Celery(
    'tasks',
    broker='redis://cache:6379/0', # 本地使用localhost:6379/0
    backend='redis://cache:6379/0' # 本地使用localhost:6379/0
)


@app.task
def add(*args):
    return args[0] + args[1]


@app.task
def star(*args):
    for i in range(1, args[0]+1):
        print(' ' * (args[0] + 1 - i) + '*' * i)
    return 'ok'


@app.task
def task_update(args):
    result = AsyncResult(args)
    return result.state

