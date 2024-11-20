from core.models.profile.db import Profile
from core.dto.profile import add_profile
from datetime import datetime
from loguru import logger

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from database import Session



# Функция для создания профиля
async def create_profile(data: add_profile.new_profile, db: AsyncSession):
    print(db)
        # Создаем объект профиля
    profile = Profile(
            phone=data.phone,
            username=data.username,
            email=data.email,
            password=data.password,
            date_created=datetime.utcnow(),  # Используем текущее время
            date_modified=datetime.utcnow(),
            balance=400
        )
    try:
        print(type(db))
            # Выполняем простой запрос через сессию
        result = await db.execute(text("SELECT * FROM profile LIMIT 10"))
        print(db)
        logger.info("Соединение с базой данных успешно установлено!")
    except Exception as e:
        print("ODODODODOOD")
        logger.error(f"Ошибка подключения к базе данных: {e}")
    return profile  # Возвращаем профиль
