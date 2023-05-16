from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='row 1, button 1'
        ),
        KeyboardButton(
            text='row 1, button 2'
        ),
        KeyboardButton(
            text='row 1, button 3'
        )
    ],
    [
        KeyboardButton(
            text='row 2, button 1'
        ),
        KeyboardButton(
            text='row 2, button 2'
        ),
        KeyboardButton(
            text='row 2, button 3'
        )
    ],
    [
        KeyboardButton(
            text='row 3, button 1'
        ),
        KeyboardButton(
            text='row 3, button 2'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Choose button:', selective=True)