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


import os
from pyrogram.filters import create
from pyrogram.types import Message, CallbackQuery

from menfess import GenshinMF
from menfess.bot import enums
from menfess.bot.templates import ON_FAILED_POST


def callback(data):
	async def func(_, __, cq: CallbackQuery):
		return data in cq.data and str(cq.from_user.id) in cq.data

	return create(func)


def restricted_for(restriction: enums.Account):
	async def func(_, c: GenshinMF, m: Message):
		user = m.from_user
		b = await c.download_media(user.photo.big_file_id, in_memory=True)
		u = await c.db.find(user.id)

		if not u:
			await c.db.create_user(user, bytes(b.getbuffer()))
			return True

		if restriction == enums.Account.BANNED:
			return not u.banned.is_banned

		if restriction == enums.Account.PARTNERSHIP:
			# TODO: Add database model for user partnership,
			# more likely this will be unused.
			return False

	return create(func)


async def valid_only_flt(_, c: GenshinMF, m: Message):
	user = m.from_user
	fail_msg = ON_FAILED_POST.format(user_id=user.id)
	ch_usn = os.getenv("CHANNEL_USERNAME")
	mem_ids = [mem.user.id async for mem in c.get_chat_members(ch_usn)]

	if (
		len(m.text.split()) >= 5 and len(m.text) >= 20 and bool(user.photo) and
		bool(user.username) and user.id in mem_ids
	):
		return True

	await m.reply(fail_msg, disable_web_page_preview=True, disable_notification=True)
	return False

valid_only = create(valid_only_flt)
