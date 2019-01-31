from project.settings import *  # noqa

DEBUG = True
CELERY_TASK_ALWAYS_EAGER = True
REDIS_URL += "-test"
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
MEDIA_ROOT = os.path.join(MEDIA_ROOT, "test")
