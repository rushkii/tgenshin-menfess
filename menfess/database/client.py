import os
from pymongo import MongoClient


class MongoDB:
	def __init__(self, conn: "MongoClient") -> None:
		self.conn = conn
		self._db = conn[os.getenv("DB_NAME")]
		self.users = self._db.users


	async def init(self):
		await self.users.create_index("id", unique=True)
		await self.users.create_index("username", unique=True)
