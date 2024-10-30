from database import Base

from sqlalchemy import Column, Integer, String, Boolean, BigInteger, NUMERIC, DATETIME, TEXT, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

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
