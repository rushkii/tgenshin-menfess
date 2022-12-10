from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from menfess.bot import custom_filters
from menfess.bot.templates import ON_HOWTO_CB
from menfess.bot.client import GenshinMF


@GenshinMF.on_callback_query(custom_filters.callback("howto"))
async def on_howto_callback(_, cq: CallbackQuery):
	user_id = cq.from_user.id
	msg = ON_HOWTO_CB.format(user_id=user_id)
	await cq.edit_message_text(
		text=msg,
		reply_markup=InlineKeyboardMarkup(
			[[InlineKeyboardButton(
				"◀️ Kembali",
				callback_data=f"start {user_id}"
			)]]
		),
		disable_web_page_preview=True
	)
