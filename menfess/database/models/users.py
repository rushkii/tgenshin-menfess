from typing import Optional
from datetime import datetime
from menfess.database.models import BaseModel


class BannedUser(BaseModel):
	is_banned: bool
	since: Optional[datetime] = None
	until: Optional[datetime] = None

	def __init__(
		self,
		is_banned: bool,
		since: Optional[datetime] = None,
		until: Optional[datetime] = None
	) -> None:
		kwargs = locals()
		kwargs.pop("self")
		super().__init__(**kwargs)


class PremiumUser(BaseModel):
	is_active: bool
	subscription_created: Optional[datetime] = None
	subscription_ended: Optional[datetime] = None

	def __init__(
		self,
		is_active: bool,
		subscription_created: Optional[datetime] = None,
		subscription_ended: Optional[datetime] = None
	) -> None:
		kwargs = locals()
		kwargs.pop("self")
		super().__init__(**kwargs)


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
