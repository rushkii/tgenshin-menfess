from typing import Union
from pyrogram import Client

from menfess.database import MongoDB


class GenshinMF(Client):
	def __init__(
		self,
		name: str,
		mongo: MongoDB,
		api_id: Union[int, str] = None,
		api_hash: str = None,
		bot_token: str = None,
		plugins: dict = None,
	):
		super().__init__(
			name=name,
			api_id=api_id,
			api_hash=api_hash,
			bot_token=bot_token,
			plugins=plugins,
		)
		self.db = mongo
