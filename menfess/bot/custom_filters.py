from pyrogram.filters import create
from pyrogram.types import Message, CallbackQuery

from menfess import GenshinMF
from menfess.bot import enums


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
