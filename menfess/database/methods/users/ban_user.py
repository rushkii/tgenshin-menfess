from pyrogram.types import User
from datetime import datetime
from datetime import timedelta

import menfess
from menfess.database.models import (
	BannedUser, UserModel
)


class BanUser:
	async def ban_user(
		self: "menfess.database.UserRepository",
		user: User,
		duration: timedelta,
		photo: bytes
	):
		usr = await self.find(user.id)
		if usr:
			if not usr.banned.is_banned:
				now = datetime.now()
				banned = BannedUser(
					is_banned=True,
					since=now,
					until=(now + duration)
				)
				model = UserModel(
					id=user.id,
					username=user.username,
					first_name=user.first_name,
					last_name=user.last_name,
					phone_number=user.phone_number,
					photo=photo,
					banned=banned,
					updated_at=now
				)
				succeed = await self.update(model.dict())
				if succeed:
					return banned
