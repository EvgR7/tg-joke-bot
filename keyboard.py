from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def control_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
                                [InlineKeyboardButton(text='Random Joke', callback_data='JOKE')],
                                [InlineKeyboardButton(text='Joke on Word', callback_data='JOKEONWORD')],
                                [InlineKeyboardButton(text='Dictionary', callback_data='DICTIONARY')],
                                [InlineKeyboardButton(text='Translate', callback_data='TRANSLATE')]
                                ])