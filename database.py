import json

from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker
from config import Config
from loguru import logger

# Базовый класс для моделей??
class Base(AsyncAttrs, DeclarativeBase):
    pass
print(Config.postgres_url)

engine = create_async_engine(str(Config.postgres_url), pool_size=20, max_overflow=0)

Session = async_sessionmaker(engine, expire_on_commit=False)



# тестовая проверка подключения
"""
async def get_data():
    # Асинхронный контекстный менеджер
    async with Session(autoflush=False, bind=engine) as db:
        task1 = Task(id = 1, text = "eeeee", till_dt=datetime.now())
        db.add(task1)
        await db.commit()
asyncio.run(get_data())
"""