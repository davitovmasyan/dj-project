import os
import shutil


def pytest_sessionfinish(session, exitstatus):
    shutil.rmtree(os.path.join(os.path.dirname(os.path.abspath(__file__)), "media/test"), ignore_errors=True)
