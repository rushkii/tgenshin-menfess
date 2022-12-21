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


from typing import Optional
from datetime import datetime
from menfess.database.models import BaseModel


class BannedUser(BaseModel):
	is_banned: bool
	since: Optional[datetime] = None
	until: Optional[datetime] = None

	def __init__(
		self,
		is_banned: bool,
		since: Optional[datetime] = None,
		until: Optional[datetime] = None
	) -> None:
		kwargs = locals()
		kwargs.pop("self")
		super().__init__(**kwargs)


class PremiumUser(BaseModel):
	is_active: bool
	subscription_created: Optional[datetime] = None
	subscription_ended: Optional[datetime] = None

	def __init__(
		self,
		is_active: bool,
		subscription_created: Optional[datetime] = None,
		subscription_ended: Optional[datetime] = None
	) -> None:
		kwargs = locals()
		kwargs.pop("self")
		super().__init__(**kwargs)


class UserModel(BaseModel):
	id: int
	username: str
	first_name: str
	last_name: Optional[str] = None
	phone_number: Optional[str] = None
	photo: bytes
	banned: Optional[BannedUser] = None
	premium: Optional[PremiumUser] = None
	created_at: Optional[datetime] = None
	updated_at: datetime

	def __init__(
		self,
		id: int,
		username: str,
		first_name: str,
		photo: bytes,
		updated_at: datetime,
		last_name: str,
		phone_number: str,
		banned: Optional[BannedUser] = None,
		premium: Optional[PremiumUser] = None,
		created_at: Optional[datetime] = None,
	) -> None:
		# we want to call the UserModel with all arguments hint,
		# then simply just get all arguments with locals(),
		# instead of pass them 1 by 1 to the super().__init__() kwargs.

		kwargs = locals()
		kwargs.pop("self")

		super().__init__(**kwargs)
