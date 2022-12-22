#  TGenshin Menfess - A Telegram bot for Genshin Impact "Mention and Confess"
#  Copyright (C) 2022-present Kiizuha <https://github.com/rushkii>
#
#  This file is part of tgenshin-menfess.
#
#  tgenshin-menfess is free software: you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  tgenshin-menfess is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with tgenshin-menfess. If not, see <https://www.gnu.org/licenses/>.
#
#  DO NO SELL OR RESELL THIS PROGRAM, THIS PROGRAM IS FOR EDUCATIONAL PURPOSE ONLY
#  AND PERSONAL USE ONLY. YOU CAN USE THIS PROGRAM AND MONETIZE IT LIKE A DONATION
#  FOR YOUR BOT AND YOUR SERVER HOSTING USING MY SCRIPTS. BUT, YOU SHOULD PUT
#  MY AUTHOR NAME IN YOUR BOT DESCRIPTION, ABOUT, ETC. YOU SHOULD PUT MY EMAIL
#  <kiizuha@gnuweeb.org> AND MY GITHUB <https://github.com/rushkii> IN YOUR BOT DESC
#  AND REMAIN KEEP OF MY LICENSE NOTICE.


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
		if not usr:
			return

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
