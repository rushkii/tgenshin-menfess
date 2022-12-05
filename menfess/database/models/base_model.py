import json
import base64
from enum import Enum
from datetime import datetime
from pydantic import BaseModel as BM


class BaseModel(BM):

	@staticmethod
	def default(obj: "BaseModel"):
		if isinstance(obj, bytes):
			# from current use case,
			# bytes obj is just for base64.
			b64 = base64.b64encode(obj)
			return b64.decode()
		if isinstance(obj, Enum):
			return str(obj)
		if isinstance(obj, datetime):
			return str(obj)

		return {
			"_": obj.__class__.__name__,
			**{
				attr: getattr(obj, attr)
				for attr in filter(lambda x: not x.startswith("_"), obj.__dict__)
				if getattr(obj, attr) is not None
			}
		}


	def __repr__(self) -> str:
		return json.dumps(self, indent=4, default=BaseModel.default, ensure_ascii=False)


	def __str__(self) -> str:
		return self.__repr__()
