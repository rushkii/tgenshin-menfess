import json
import base64
from enum import Enum
from datetime import datetime
from pydantic import BaseModel as BM


class BaseModel(BM):
	def __repr__(self) -> str:
		new_d = self.dict().copy()
		for k,v in self.dict().items():
			if isinstance(v, bytes):
				b64 = base64.b64encode(v)
				new_d[k] = b64.decode()
			if isinstance(v, Enum):
				new_d[k] = str(v)
			if isinstance(v, datetime):
				new_d[k] = str(v)
			if not v:
				new_d.pop(k)

		return json.dumps(new_d, indent=4, ensure_ascii=False)


	def __str__(self) -> str:
		return self.__repr__()
