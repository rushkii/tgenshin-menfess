#  TGenshin Menfess - A Telegram bot for Genshin Impact "Mention and Confess"
#  Copyright (C) 2022-present Kiizuha <https://github.com/rushkii>
#
#  This file is part of tgenshin-menfess.
#
#  tgenshin-menfess is free software: you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  tgenshin-menfess is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with tgenshin-menfess. If not, see <https://www.gnu.org/licenses/>.
#
#  DO NO SELL OR RESELL THIS PROGRAM, THIS PROGRAM IS FOR EDUCATIONAL PURPOSE ONLY
#  AND PERSONAL USE ONLY. YOU CAN USE THIS PROGRAM AND MONETIZE IT LIKE A DONATION
#  FOR YOUR BOT AND YOUR SERVER HOSTING USING MY SCRIPTS. BUT, YOU SHOULD PUT
#  MY AUTHOR NAME IN YOUR BOT DESCRIPTION, ABOUT, ETC. YOU SHOULD PUT MY EMAIL
#  <kiizuha@gnuweeb.org> AND MY GITHUB <https://github.com/rushkii> IN YOUR BOT DESC
#  AND REMAIN KEEP OF MY LICENSE NOTICE.


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
