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


import os


__TRAVELER = "[Traveler](tg://user?id={user_id})"
__TEYVAT = f"[Teyvat](t.me/{os.getenv('CHANNEL_USERNAME')})"
__RULES = """- Akun Telegram {_TRV} harus follow {_TVT} dulu ya, ehe~.
- Akun Telegram {_TRV} harus memiliki username dan foto profil.
- Pesan {_TRV} harus berjumlah minimal 20 karakter dan 5 kata.""".format(_TRV=__TRAVELER, _TVT=__TEYVAT)


ON_START_MSG = """
Halo {_TRV}!, selamat datang di {bot_name}.
Aku adalah bot untuk membawa pesan kamu ke alam {_TVT},
{_TRV} kalau mau tau cara kirim pesan ke {_TVT} tinggal tekan tombol di bawah ya, ehe!
""".format(_TRV=__TRAVELER, _TVT=__TEYVAT, bot_name="{bot_name}")


ON_HOWTO_CB = """
{_TRV} tinggal ketik apapun yang {_TRV} mau yang berhubungan dengan Genshin Impact ya {_TRV}, tetapi
pesan {_TRV} akan terkirim jika pesan {_TRV} memenuhi syarat di bawah ini:

{_RULE}

Udah itu aja {_TRV}! enjoy flexing gacha dan damage karakter {_TRV} ya, ehe!
""".format(_TRV=__TRAVELER, _TVT=__TEYVAT, _RULE=__RULES)


ON_SUCCESS_POST = """
Hore, pesan {_TRV} telah terkirim ke {_TVT}!
{_TRV} bisa melihatnya dengan menekan tombol di bawah ya~.
""".format(_TRV=__TRAVELER, _TVT=__TEYVAT)


ON_FAILED_POST = """
Yah, pesan {_TRV} belum memenuhi kriteria di bawah ini:

{_RULE}

Jadi Paimon gabisa mengirim pesan {_TRV}, hiks.
""".format(_TRV=__TRAVELER, _TVT=__TEYVAT, _RULE=__RULES)
