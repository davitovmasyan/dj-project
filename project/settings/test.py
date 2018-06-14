from project.settings import *  # noqa


DEBUG = True
CELERY_TASK_ALWAYS_EAGER = True
REDIS_URL += "-test"
