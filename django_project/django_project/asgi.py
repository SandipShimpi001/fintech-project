import os
import django
from django.core.asgi import get_asgi_application
from fastapi_app.routes import fastapi_app
from starlette.routing import Mount
from starlette.applications import Starlette

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

# Get Django ASGI application
django_app = get_asgi_application()

# Mount FastAPI under /api, Django under /
app = Starlette(routes=[
    Mount("/api", app=fastapi_app),
    Mount("/", app=django_app),
])
