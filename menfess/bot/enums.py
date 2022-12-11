import enum


class BaseEnum(enum.Enum):
	def _generate_next_value_(self, *args):
		return self.lower()

	def __repr__(self):
		return f"GenshinMF.enums.{self}"


class Account(BaseEnum):
	ADMIN = enum.auto()
	BANNED = enum.auto()
	PREMIUM = enum.auto()
	PARTNERSHIP = enum.auto()
