from pyrogram import filters
from pyrogram.types import CallbackQuery


def callback(data):
	async def func(flt, _, cq: CallbackQuery):
		return flt.data in cq.data and str(cq.from_user.id) in cq.data

	return filters.create(func, data=data)
