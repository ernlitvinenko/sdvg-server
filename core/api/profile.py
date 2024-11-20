from fastapi import APIRouter, HTTPException
from core.models.profile.requests import NewProfile
from core.services.validation.validation_info import username_validation
from core.services.validation.validation_info import email_validation
from core.services.validation.validation_info import password_validation
from core.storage import profile_storage
router = APIRouter()


@router.get("/profile")
def get_info():
    return 0


@router.post("/add_profile")
async def create_profile(profile: NewProfile):
    if not username_validation(profile.username):
        raise HTTPException(status_code=422, detail="The username is not entered correctly")
    if not email_validation(profile.email):
        raise HTTPException(status_code=422, detail="The email is not entered correctly")
    if not password_validation(profile.password):
        raise HTTPException(status_code=422, detail="The password is not entered correctly")

    return await profile_storage.create_profile(profile)
    """Какие-нибудь токены сюда вставить надо"""
