from typing import Optional
from datetime import datetime
from menfess.database.models import BaseModel


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
