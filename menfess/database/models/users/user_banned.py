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
