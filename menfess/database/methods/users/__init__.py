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


from pymongo.errors import DuplicateKeyError

import menfess
from .ban_user import BanUser
from .create_user import CreateUser
from menfess.database.models import UserModel


class UserRepository(BanUser, CreateUser):
	async def find(self: "menfess.MongoDB", id: int):
		res = await self.users.find_one({"id": id})
		if res:
			res = res.copy()
			res.pop("_id")
			return UserModel(**res)


	async def save(self: "menfess.MongoDB", data: dict):
		async with await self.conn.start_session() as s:
			async with s.start_transaction():
				try:
					res = await self.users.insert_one(data)
					return bool(res.inserted_id)
				except DuplicateKeyError:
					return None


	async def update(self: "menfess.MongoDB", data: dict):
		async with await self.conn.start_session() as s:
			async with s.start_transaction():
				d = data.copy()
				for k,v in data.items():
					if v is None:
						d.pop(k)
				r = await self.users.update_one(
					filter={"id": d['id']},
					update={"$set": d}
				)
				return r.matched_count > 0
