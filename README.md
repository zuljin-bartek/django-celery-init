# Template for Django+celery project

A minimalistic project starter for Django+celery application.


## Installing requirements

The settings file assumes that `rabbitmq-server` is running on `localhost` using the default ports. More information here:

http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html

In addition, some Python requirements must also be satisfied:

```console
pip install -r requirements.txt
```

## Quick start

Before adding new project's bits, there are few things that should be changed:

* watchdog/settings.py
    * Generate new `SECRET_KEY` (this one can be used in development phase)
    * Add admin to `ADMINS` section
    * Uncomment and edit Email settings
    * Add/edit/remove app in `INSTALLED_APPS`
    * Verify and edit `CELERY_BROKER_URL` if you are using other message broker, etc.
* watchdog/urls.py
    * Modify app urls

To test whole project you should start few components (Django app, celery worker and beat).

Before you start Django app you should at least call following commands in project root:
```
python manage.py makemigrations

python manage.py migrate
```

After that start Django test server (defaults to `localhost:8000`):
```
python manage.py runserver
```

To start Celery worker:
```
celery -A watchdog worker -l info
```

and to start beat:
```
celery -A watchdog beat -l info -S django
```


## TODO

* Add miniscript to rename project and initial app.

