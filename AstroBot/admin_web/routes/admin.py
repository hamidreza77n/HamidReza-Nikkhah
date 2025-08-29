from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER
from AstroBot.core.database import SessionLocal
from AstroBot.models.user_model import User

router = APIRouter()

def admin_required(request: Request):
    if not request.session.get("admin"):
        return RedirectResponse("/login", status_code=HTTP_303_SEE_OTHER)

@router.get("/admin/dashboard")
async def dashboard(request: Request):
    admin_required(request)
    session = SessionLocal()
    users = session.query(User).all()
    session.close()
    return request.app.templates.TemplateResponse("admin_dashboard.html", {"request": request, "users": users})

@router.get("/admin/approve/{user_id}")
async def approve_user(request: Request, user_id: int):
    admin_required(request)
    session = SessionLocal()
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        user.is_approved = True
        session.commit()
    session.close()
    return RedirectResponse("/admin/dashboard", status_code=HTTP_303_SEE_OTHER)

@router.get("/admin/reject/{user_id}")
async def reject_user(request: Request, user_id: int):
    admin_required(request)
    session = SessionLocal()
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
    session.close()
    return RedirectResponse("/admin/dashboard", status_code=HTTP_303_SEE_OTHER)
