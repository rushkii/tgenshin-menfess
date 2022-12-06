from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from . import filter
from menfess.bot.templates import ON_START_MSG
from menfess.bot.client import GenshinMF


@GenshinMF.on_callback_query(filter.callback("start"))
async def on_start_callback(c: GenshinMF, cq: CallbackQuery):
	user_id = cq.from_user.id
	msg = ON_START_MSG.format(user_id=user_id, bot_name=c.me.first_name)
	await cq.edit_message_text(
		text=msg,
		reply_markup=InlineKeyboardMarkup(
			[[InlineKeyboardButton(
				"Gimana caranya?",
				callback_data=f"howto {user_id}"
			)]]
		),
		disable_web_page_preview=True
	)
