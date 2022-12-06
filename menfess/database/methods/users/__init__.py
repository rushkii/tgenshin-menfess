from pymongo.errors import DuplicateKeyError

import menfess
from .ban_user import BanUser
from .create_user import CreateUser
from menfess.database.models import UserModel


class UserRepository(BanUser, CreateUser):
	async def find(self: "menfess.MongoDB", id: int):
		res = await self.users.find_one({"id": id})
		if res:
			res = res.copy()
			res.pop("_id")
			return UserModel(**res)


	async def save(self: "menfess.MongoDB", data: dict):
		async with await self.conn.start_session() as s:
			async with s.start_transaction():
				try:
					res = await self.users.insert_one(data)
					return bool(res.inserted_id)
				except DuplicateKeyError:
					return None


	async def update(self: "menfess.MongoDB", data: dict):
		async with await self.conn.start_session() as s:
			async with s.start_transaction():
				d = data.copy()
				for k,v in data.items():
					if v is None:
						d.pop(k)
				r = await self.users.update_one(
					filter={"id": d['id']},
					update={"$set": d}
				)
				return r.matched_count > 0
