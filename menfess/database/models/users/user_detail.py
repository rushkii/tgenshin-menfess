from typing import Optional
from datetime import datetime

from menfess.database.models import BaseModel
from menfess.database.models.users import BannedUser, PremiumUser


class UserModel(BaseModel):
	id: int
	username: str
	first_name: str
	last_name: Optional[str] = None
	phone_number: Optional[str] = None
	photo: bytes
	banned: Optional[BannedUser] = None
	premium: Optional[PremiumUser] = None
	created_at: Optional[datetime] = None
	updated_at: datetime

	def __init__(
		self,
		id: int,
		username: str,
		first_name: str,
		photo: bytes,
		updated_at: datetime,
		last_name: str,
		phone_number: str,
		banned: Optional[BannedUser] = None,
		premium: Optional[PremiumUser] = None,
		created_at: Optional[datetime] = None,
	) -> None:
		# we want to call the UserModel with all arguments hint,
		# then simply just get all arguments with locals(),
		# instead of pass them 1 by 1 to the super().__init__() kwargs.

		kwargs = locals()
		kwargs.pop("self")

		super().__init__(**kwargs)
