from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER
from starlette.middleware.sessions import SessionMiddleware
from AstroBot.config import ADMIN_WEB_PASSWORD

router = APIRouter()

@router.get("/login")
async def login_page(request: Request):
    return request.app.templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
async def login_action(request: Request, password: str = Form(...)):
    if password == ADMIN_WEB_PASSWORD:
        request.session["admin"] = True
        return RedirectResponse("/admin/dashboard", status_code=HTTP_303_SEE_OTHER)
    return request.app.templates.TemplateResponse("login.html", {"request": request, "error": "رمز اشتباه است"})

@router.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/login", status_code=HTTP_303_SEE_OTHER)
