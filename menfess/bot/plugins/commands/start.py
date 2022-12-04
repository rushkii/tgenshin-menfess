from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from menfess.bot.templates import ON_START_MSG


@Client.on_message(filters.command("start") & filters.private)
async def on_start_command(c: Client, m: Message):
	user_id = m.from_user.id
	msg = ON_START_MSG.format(
		user_id=user_id,
		bot_name=c.me.first_name,
		channel_link="t.me/teyvat_realm"
	)
	await m.reply(msg, reply_markup=InlineKeyboardMarkup(
		[[InlineKeyboardButton(
			"Gimana caranya? 🤔",
			callback_data=f"howto {user_id}"
		)]]
	))
