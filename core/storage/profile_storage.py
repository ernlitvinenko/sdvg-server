from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseStorage
from ..models.profile.requests import CreateProfileRequest
from ..models.profile.responses import CreateProfileResponse


class ProfileStorage(BaseStorage):
    async def create_profile(self, profile: CreateProfileRequest) -> CreateProfileResponse:
        stmt = text("""
        insert into profile (phone, username, password, email, balance) values  (
        :phone, :username, :password, :email, :balance
        )
        """)

        stmt_select = text(f"""
            select * from profile where phone ='{profile.phone}' limit 1
        """)

        async with self.get_session() as session:
            session: AsyncSession
            profile_data_query = profile.model_dump(mode="python")
            profile_data_query["balance"] = 400

            await session.execute(stmt, profile_data_query)
            await session.commit()

            d = (await session.execute(stmt_select)).fetchone()
            return CreateProfileResponse(id=d.id, phone=d.phone, username=d.username, password=d.password,
                                         email=d.email)
