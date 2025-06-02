from invoke import task

@task
def start_api(c):
    c.run('uvicorn app.main:app --reload --host 127.0.0.1 --port 8000')

@task
def start_oauth(c):
    c.run('uvicorn app.auth.oauth_server:app --reload --host 127.0.0.1 --port 8001')

@task
def start_worker(c):
    c.run('celery -A celery_app.worker worker --loglevel=info')

@task
def start_slack(c):
    c.run('python slack/bolt_app.py')
