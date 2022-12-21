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


from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from menfess.bot.templates import ON_START_MSG
from menfess.bot.client import GenshinMF


@GenshinMF.on_message(filters.command("start") & filters.private)
async def on_start_command(c: GenshinMF, m: Message):
	user_id = m.from_user.id
	msg = ON_START_MSG.format(user_id=user_id, bot_name=c.me.first_name)
	await m.reply(
		text=msg,
		reply_markup=InlineKeyboardMarkup(
			[[InlineKeyboardButton(
				"Gimana caranya? 🤔",
				callback_data=f"howto {user_id}"
			)]]
		),
		disable_web_page_preview=True
	)
