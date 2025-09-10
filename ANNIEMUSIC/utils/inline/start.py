from pyrogram.types import InlineKeyboardButton

import config
from ANNIEMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHANNEL),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            # 🔧 FIXED HERE (changed from user_id=... to url="tg://user?id=...")
            InlineKeyboardButton(text=_["S_B_7"], url=f"tg://user?id={config.OWNER_ID}"),
            InlineKeyboardButton(text=_["S_B_4"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["S_B_3"], callback_data="open_help"),
        ],
    ]
    return buttons
