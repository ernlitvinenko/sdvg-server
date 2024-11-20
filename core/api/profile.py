from fastapi import APIRouter, HTTPException
from core.models.profile.requests import CreateProfileRequest
from core.storage import profile_storage

router = APIRouter()


@router.get("/profile")
def get_info():
    return 0


@router.post("/profile")
async def create_profile(profile: CreateProfileRequest):
    return await profile_storage.create_profile(profile)
    # TODO Какие-нибудь токены сюда вставить надо
