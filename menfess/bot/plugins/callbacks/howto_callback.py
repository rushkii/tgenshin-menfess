from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from . import filter
from menfess.bot.templates import ON_HOWTO_CB


@Client.on_callback_query(filter.callback("howto"))
async def on_howto_callback(_, cq: CallbackQuery):
	user_id = cq.from_user.id
	msg = ON_HOWTO_CB.format(user_id=user_id)
	await cq.edit_message_text(msg, reply_markup=InlineKeyboardMarkup(
		[[InlineKeyboardButton(
			"◀️ Kembali",
			callback_data=f"start {user_id}"
		)]]
	))
