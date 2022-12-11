import os
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from menfess.bot.templates import ON_SUCCESS_POST
from menfess.bot.client import GenshinMF
from menfess.bot import custom_filters, enums


@GenshinMF.on_message(
	(filters.text | filters.photo | filters.video | filters.document) &
	filters.private & (
		custom_filters.restricted_for(enums.Account.BANNED) &
		custom_filters.valid_only
	)
)
async def on_post_menfess(_, m: Message):
	user = m.from_user
	ch_usn = os.getenv("CHANNEL_USERNAME")

	copied = await m.copy(ch_usn)
	await m.reply(
		text=ON_SUCCESS_POST.format(user_id=user.id),
		reply_markup=InlineKeyboardMarkup(
			[[InlineKeyboardButton(
				"Lihat pesan 💬",
				url=f"t.me/{ch_usn}/{copied.id}"
			)]]
		),
		disable_web_page_preview=True,
		disable_notification=True
	)
