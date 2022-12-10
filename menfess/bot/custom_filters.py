from pyrogram.filters import create
from pyrogram.types import CallbackQuery


def callback(data):
	async def func(_, __, cq: CallbackQuery):
		return data in cq.data and str(cq.from_user.id) in cq.data

	return create(func)
