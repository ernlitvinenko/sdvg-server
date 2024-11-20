# api/__init__.py
from fastapi import APIRouter
from .profile import router as profile_router  # Импортируем роутер из profile

# Создаем главный роутер с префиксом '/api/v1'
router = APIRouter(prefix="/api")

# Подключаем роутер профиля к главному роутеру
router.include_router(profile_router)
