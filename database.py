import json

import asyncpg
from sqlalchemy import Column, Integer, String, Boolean, BigInteger, NUMERIC, DATETIME, TEXT, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
import asyncio
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


# типо так подключать модельки???
class AchievementProfile(Base):
    """ """
    __tablename__ = "achievement_profile"
    profile_id = Column(Integer, primary_key=True, nullable=False)
    achievement_id = Column(Integer, primary_key=True, nullable=False)

    #profile_id = Column(Integer, ForeignKey("profile.id"), nullable=False)
    #achievement_id = Column(Integer, ForeignKey("achievement.id"), nullable=False)
    
    # отношения между таблицами??
    #profiles = relationship("Profile", back_populates="profile")
    #achievements = relationship("Achievement", back_populates="achievement")

class Profile(Base):
    """ """
    __tablename__ = "profile"
    id = Column(Integer, primary_key=True, nullable=False)
    phone = Column(BigInteger, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    date_created = Column(DATETIME, default=datetime.now())
    date_modified = Column(DATETIME, default=datetime.now())
    #del = Column(Boolean, nullable=False, default=False) # del - это вообще ключевое слово, так то
    balance = Column(NUMERIC, nullable=False, default=0)

    # отношения между таблицами??
    #achievements_profiles = relationship("AchievementProfile", back_populates="achievement_profile")


class Lst(Base):
    """ """
    __tablename__ = "lst"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
    date_created = Column(DATETIME, default=datetime.now())
    date_modified = Column(DATETIME, default=datetime.now())
    #del = Column(Boolean, nullable=False, default=False) # del - это вообще ключевое слово, так то

class LstValue(Base):
    """ """
    __tablename__ = "lst_value"
    id = Column(Integer, primary_key=True, nullable=False)
    lst_id = Column(Integer, ForeignKey("lst.id"), nullable=False)
    name = Column(String, nullable=False)
    date_created = Column(DATETIME, default=datetime.now())
    date_modified = Column(DATETIME, default=datetime.now())
    #del = Column(Boolean, nullable=False, default=False) # del - это вообще ключевое слово, так то

    lsts = relationship("Lst", back_populates="lst")

class Task(Base):
    """ """
    __tablename__ = "task"
    id = Column(Integer, primary_key=True, nullable=False)
    profile_id = Column(Integer, ForeignKey("profile.id"))
    title = Column(String)
    text = Column(TEXT, nullable=False)
    till_dt = Column(DATETIME, nullable=False)
    completed_dt = Column(DATETIME)
    date_created = Column(DATETIME, default=datetime.now())
    date_modified = Column(DATETIME, default=datetime.now())

    profiles = relationship("Profile", back_populates="profile")


class Transaction(Base):
    """ """
    __tablename__ = "transaction"
    id = Column(Integer, primary_key=True, nullable=False)
    value = Column(NUMERIC, default=0, nullable=False)
    date_created = Column(DATETIME, default=datetime.now())
    date_modified = Column(DATETIME, default=datetime.now())


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