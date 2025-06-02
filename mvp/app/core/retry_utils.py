# app/core/retry_utils.py

from functools import wraps
import requests

def clio_api_retry(task_self=None):
    """
    Decorator to retry Clio API service methods if token expired (401) or temporary errors occur.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(service, *args, **kwargs):
            try:
                return func(service, *args, **kwargs)

            except requests.exceptions.HTTPError as exc:
                if exc.response.status_code == 401:
                    print("🔄 Token expired, refreshing and retrying...")
                    service.refresh_client()
                    return func(service, *args, **kwargs)

                elif 500 <= exc.response.status_code < 600 and task_self is not None:
                    print(f"🔁 Server error ({exc.response.status_code}), retrying task...")
                    raise task_self.retry(exc=exc)

                else:
                    raise  # Let other HTTP errors bubble up

            except Exception as exc:
                if task_self is not None:
                    print("⚠️ Unexpected error, retrying task...")
                    raise task_self.retry(exc=exc)
                raise

        return wrapper
    return decorator