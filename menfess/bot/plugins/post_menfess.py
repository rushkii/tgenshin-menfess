import os
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from menfess.bot.templates import ON_SUCCESS_POST
from menfess.bot.client import GenshinMF


@GenshinMF.on_message(
	(filters.text | filters.photo | filters.video | filters.document) &
	filters.private
)
async def on_post_menfess(c: GenshinMF, m: Message):
	if len(m.text.split()) >= 5 and len(m.text) >= 20:
		ch_usn = os.getenv("CHANNEL_USERNAME")
		mem_ids = [mem.user.id async for mem in c.get_chat_members(ch_usn)]
		if m.from_user.id in mem_ids:
			copied = await m.copy(ch_usn)
			msg = ON_SUCCESS_POST.format(user_id=m.from_user.id)
			await m.reply(
				text=msg,
				reply_markup=InlineKeyboardMarkup(
					[[InlineKeyboardButton(
						"Lihat pesan 💬",
						url=f"t.me/{ch_usn}/{copied.id}"
					)]]
				),
				disable_web_page_preview=True
			)
