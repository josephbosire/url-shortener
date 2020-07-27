"""
ASGI config for tapper_portal project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tinyurl.settings")

routes = [
    Mount("/static", app=StaticFiles(directory="/static"), name="static"),
    Mount("/", app=get_asgi_application(), name="django"),
]

application = Starlette(routes=routes)
