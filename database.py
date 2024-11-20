import json
import asyncio
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker
from config import Config
from loguru import logger

# Базовый класс для моделей??
class Base(AsyncAttrs, DeclarativeBase):
    pass

engine = create_async_engine(str(Config.postgres_url), pool_size=20, max_overflow=0)

Session = async_sessionmaker(bind=engine, expire_on_commit=False)
async def get_session() -> AsyncSession:
    try:
        async with Session() as session:
            yield session
    except Exception as e:
        logger.error(f"Error in get_session: {e}")
        raise

async def check_db_session():
    async with Session() as session:
        try:
            print(session)
            # Выполняем простой запрос через сессию
            result = await session.execute(text("SELECT * FROM profile LIMIT 10"))
            print(result)
            logger.info("Соединение с базой данных успешно установлено!")
        except Exception as e:
            logger.error(f"Ошибка подключения к базе данных: {e}")

# Запуск проверки
asyncio.run(check_db_session())
