# Copyright (C) 2018 - 2020 MrYacha. All rights reserved. Source code available under the AGPL.
# Copyright (C) 2021 TeamDaisyX
# Copyright (C) 2020 Inuka Asith

# This file is part of Daisy (Telegram Bot)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import random
from contextlib import suppress

from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import MessageNotModified

from DaisyX.decorator import register
from DaisyX.modules.utils.disable import disableable_dec

from . import MOD_HELP
from .language import select_lang_keyboard
from .utils.disable import disableable_dec
from .utils.language import get_strings_dec

helpmenu_cb = CallbackData("helpmenu", "mod")


def help_markup(modules):
    markup = InlineKeyboardMarkup()
    for module in modules:
        markup.insert(
            InlineKeyboardButton(module, callback_data=helpmenu_cb.new(mod=module))
        )
    return markup


STICKERS = (
    "CAACAgIAAxkBAAICdWC2edwaC1hj5tD2FTtydWE6sAO1AAKjAQACEBptIkfOxfML2NdjHwQ",
    "CAACAgIAAxkBAAICeGC2efBa2B_L55WpbcagcGBzzot4AAJ6AQACEBptIpydt0hO73LeHwQ",
    "CAACAgIAAxkBAAICeWC2egSQp-jkQFMW_9d-pnv2sIOwAAJoAQACEBptIvU3HCn2F6RvHwQ",
    "CAACAgIAAxkBAAICemC2egTl3ry5VSWSb8AmtDDmOP3RAAJpAQACEBptItP50YqvnDOtHwQ",
    "CAACAgIAAxkBAAICe2C2egRND4q_KohS1EAfOkaoGromAAJeAQACEBptItNORzH8jWOyHwQ",
    "CAACAgIAAxkBAAICfGC2egbdINXuuuvaUV0UmPYXKqrEAAJZAQACEBptIh2VbDlfzkAfHwQ",
    "CAACAgIAAxkBAAICfWC2eg5wUklnzGIhZtlstAO65AEnAAJ1AQACEBptInCKj7c5KByPHwQ",
    "CAACAgIAAxkBAAICfmC2ehA5DUhuvj8NqI_R0OW0BypiAAJXAQACEBptIqUrPFT7ejSqHwQ",
    "CAACAgIAAxkBAAICf2C2ehJl3LsbLlK9B8FC3UFlFHLfAAJ5AQACEBptIrh-txD7aZGTHwQ",
    "CAACAgIAAxkBAAICgGC2eixmDbpc3Cj1z-2SajCMlHwRAAJTAQACEBptIusJVTXP9-ZJHwQ",
    "CAACAgIAAxkBAAICgWC2ejoKHhYxPp8YmUqrjddmK-j3AAJmAQACEBptIgELm-YRAtc5HwQ",
    "CAACAgIAAxkBAAICgmC2ejy-3WNj7AW6n0HJnKHNZwrnAAKSAQACEBptIuuEW7yIvJNpHwQ",
    "CAACAgIAAxkBAAICg2C2ekQ64wfSzD7H9mUwFKRyv99bAAKpAQACEBptIsp-kz6P8Yg3HwQ",
    "CAACAgIAAxkBAAIChWC2ekaOmPF44EtK5gaGPp4nbfEBAAJ5AQACEBptIrh-txD7aZGTHwQ",
    "CAACAgIAAxkBAAIChmC2emDLLWY-WNbNDHNFs7dP0_2CAALIAQACEBptIg5zcps1Oc8WHwQ",
    "CAACAgUAAxkBAAICh2C2epS0NTXI5wjdhmT4GVsCMxc1AAJmAQACaFT5Vd-coYpBjPcDHwQ",
    "CAACAgUAAxkBAAICiGC2epeJUBKTKA34q_JcLCvwd-RYAAIvAQACJSX4VTQhEYMYTbB2HwQ",
    "CAACAgUAAxkBAAICimC2eqiUXsLnA7bp_gABFF2-n_dQxgACLgIAAkid-VUoAtdfzSB7Dx8E",
    "CAACAgUAAxkBAAICi2C2eshXjWebgg0VGcJKUHrNynZZAALWAAMiVYE1SHwr-xT2vPYfBA",
    "CAACAgUAAxkBAAICumC2fOVz4FBjVOJ1hujVuKRdvMlvAAI6AgACXWoJV-gIqrglf23zHwQ",
    "CAACAgUAAxkBAAICu2C2fOd1vNLl9vJtVXbYKqKYCSVbAAKfAQACjTMJV_P2fCpoFMshHwQ"

)


@register(cmds="start", no_args=True, only_groups=True)
@disableable_dec("start")
@get_strings_dec("pm_menu")
async def start_group_cmd(message, strings):
    await message.reply(strings["start_hi_group"])


@register(cmds="start", no_args=True, only_pm=True)
async def start_cmd(message):
    await message.reply_sticker(random.choice(STICKERS))
    await get_start_func(message)


@get_strings_dec("pm_menu")
async def get_start_func(message, strings, edit=False):
    msg = message.message if hasattr(message, "message") else message

    task = msg.edit_text if edit else msg.reply
    buttons = InlineKeyboardMarkup()
    buttons.add(InlineKeyboardButton(strings["btn_help"], callback_data="get_help"))
    buttons.add(
        InlineKeyboardButton(strings["btn_lang"], callback_data="lang_btn"),
        InlineKeyboardButton(
            strings["btn_source"], url="https://www.instagram.com/mr.matheesha_official/"
        ),
    )
    buttons.add(
        InlineKeyboardButton(strings["btn_channel"], url="https://t.me/CeylonTech_plus"),
        InlineKeyboardButton(
            strings["btn_group"], url="https://t.me/CeylonTech_Official"
        ),
    )
    buttons.add(
        InlineKeyboardButton("▶️Youtube", url="https://youtube.com/channel/UC04AUyOQmht0c8Bgc2GehRw"),
        InlineKeyboardButton(
            "🎭Owner", url="https://t.me/percy_jackson_4",
        ),
    )
    buttons.add(
        InlineKeyboardButton(
             "😍Add Hermione to your group",
            url=f"https://telegram.me/miss_musicybot?startgroup=true",
        ),
    )
    buttons.add(
        InlineKeyboardButton(
             "😍Add Music Assistant",
            url=f"https://telegram.me/sing_hermione?startgroup=true",
        )
    )
    # Handle error when user click the button 2 or more times simultaneously
    with suppress(MessageNotModified):
        await task(strings["start_hi"], reply_markup=buttons)


@register(regexp="get_help", f="cb")
@get_strings_dec("pm_menu")
async def help_cb(event, strings):
    button = help_markup(MOD_HELP)
    button.add(InlineKeyboardButton(strings["back"], callback_data="go_to_start"))
    with suppress(MessageNotModified):
        await event.message.edit_text(strings["help_header"], reply_markup=button)


@register(regexp="lang_btn", f="cb")
async def set_lang_cb(event):
    await select_lang_keyboard(event.message, edit=True)


@register(regexp="go_to_start", f="cb")
async def back_btn(event):
    await get_start_func(event, edit=True)


@register(cmds="help", only_pm=True)
@disableable_dec("help")
@get_strings_dec("pm_menu")
async def help_cmd(message, strings):
    button = help_markup(MOD_HELP)
    button.add(InlineKeyboardButton(strings["back"], callback_data="go_to_start"))
    await message.reply(strings["help_header"], reply_markup=button)


@register(cmds="help", only_groups=True)
@disableable_dec("help")
@get_strings_dec("pm_menu")
async def help_cmd_g(message, strings):
    text = strings["btn_group_help"]
    button = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text=text, url="https://t.me/miss_musicybot?start")
    )
    await message.reply(strings["help_header"], reply_markup=button)


@register(helpmenu_cb.filter(), f="cb", allow_kwargs=True)
async def helpmenu_callback(query, callback_data=None, **kwargs):
    mod = callback_data["mod"]
    if not mod in MOD_HELP:
        await query.answer()
        return
    msg = f"Help for <b>{mod}</b> module:\n"
    msg += f"{MOD_HELP[mod]}"
    button = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="🏃‍♂️ Back", callback_data="get_help")
    )
    with suppress(MessageNotModified):
        await query.message.edit_text(
            msg, disable_web_page_preview=True, reply_markup=button
        )
        await query.answer("Help for " + mod)
