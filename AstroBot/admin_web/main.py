from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from .routes import auth, admin

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="supersecretkey")

# templates & static
app.mount("/static", StaticFiles(directory="admin_web/static"), name="static")
app.templates = Jinja2Templates(directory="admin_web/templates")

# include routes
app.include_router(auth.router)
app.include_router(admin.router)
