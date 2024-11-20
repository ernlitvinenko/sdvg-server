from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Body
from database import get_session

from sqlalchemy.ext.asyncio import AsyncSession
#from fastapi.responses import JSONResponse
#from fastapi import status

from core.dto.profile.add_profile import NewProfile
from core.services.validation.validation_info import phone_validation
from core.services.validation.validation_info import username_validation
from core.services.validation.validation_info import email_validation
from core.services.validation.validation_info import password_validation
from core.models.profile.db import Profile
from core.services import profile as ProfileService

from sqlalchemy.orm import Session

from loguru import logger

from sqlalchemy import text


router = APIRouter()



@router.get("/profile")
def get_info():
    return 0

@router.post("/add_profile")
async def create_profile(profile: NewProfile, session: AsyncSession = Depends(get_session)):

    if not username_validation(profile.username):
        raise HTTPException(status_code=422, detail="The username is not entered correctly")
    if not email_validation(profile.email):
        raise HTTPException(status_code=422, detail="The email is not entered correctly")
    if not password_validation(profile.password):
        raise HTTPException(status_code=422, detail="The password is not entered correctly")
    
    return await ProfileService.create_profile(profile, session)
    """Какие-нибудь токены сюда вставить надо"""
