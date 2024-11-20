"""
Register our storages
"""
from .profile_storage import ProfileStorage
from .base import BaseStorage
from database import Session

base_storage = BaseStorage(Session)
profile_storage = ProfileStorage(Session)
