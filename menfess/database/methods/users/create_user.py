from pyrogram.types import User
from datetime import datetime

import menfess
from menfess.database.models import UserModel
from menfess.database.models.users import (
	BannedUser,
	PremiumUser
)


class CreateUser:
	async def create_user(self: "menfess.database.UserRepository", user: User, photo: bytes):
		now = datetime.now()
		model = UserModel(
			id=user.id,
			username=user.username,
			first_name=user.first_name,
			last_name=user.last_name,
			phone_number=user.phone_number,
			photo=photo,
			banned=BannedUser(is_banned=False),
			premium=PremiumUser(is_active=False),
			created_at=now,
			updated_at=now
		)
		succeed = await self.save(model.dict())
		if succeed:
			return model
