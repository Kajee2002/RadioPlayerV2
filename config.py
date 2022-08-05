"""
RadioPlayerV2, Telegram Voice Chat Bot
Copyright (C) 2021  Asm Safone <https://t.me/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import re


class Config:
    ADMIN = os.environ.get("ADMINS", "1757568732")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", 6309305))
    CHAT = int(os.environ.get("CHAT", "-1001529457429"))
    LOG_GROUP = os.environ.get("LOG_GROUP", "")
    if LOG_GROUP:
        LOG_GROUP = int(LOG_GROUP)
    else:
        LOG_GROUP = None
    STREAM_URL = os.environ.get("STREAM_URL", "https://radioindia.net/radio/hungamanow/icecast.audio")
    API_HASH = os.environ.get("API_HASH", "8b0473750d327598c8585b0049f09e2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5384280460:AAHcxjQJlZAcgsWOPLo9fLepLIIZRQcYbkw") 
    SESSION = os.environ.get("SESSION_STRING", "BQCKDejjL8ifbe3YyCRsi-51Em2tZjbJH2Ka7OBGnJ60jYZpXHWou2Sr-2veYm098nEHVACzUYHC1e_LZIZB6EevLeXGY0VTcGvUVg0Wo2fw11KvlmwmnFRwmWulD-N4Em0bx5b0jCowxEuWtly19UgaLaxjdmztQtYD-ARYqOka1Kev9EZQJWbS6ub9lcX4etzBJxc29P5K52izTURRsbo2dzZtnVpeM9taKk78tmR6CyAkSKP7CZBbyhFxMVNT59tkq-NZFqp_dCK9htnAY4IaM2D1x3blheyl7-Wvi9lkS1yN__X0ziiYrp3EWjUY5U4MYN7Z8e9HZxo8Tf9sJPsZaMJe3AA")

