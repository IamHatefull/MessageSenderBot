from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

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

loc_tel_poll_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(
        text='Send location',
        request_location=True
        )
    ],
    [
    KeyboardButton(
        text='Send your contact',
        request_contact=True
    )
    ],
    [
    KeyboardButton(
        text='Create quiz',
        request_poll=KeyboardButtonPollType()
    )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Choose action:'
)

def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text= 'Button 1')
    keyboard_builder.button(text= 'Button 2')
    keyboard_builder.button(text= 'Button 3')
    keyboard_builder.button(text= 'Send location', request_location=True)
    keyboard_builder.button(text= 'Send your contact', request_contact=True)
    keyboard_builder.button(text= 'Create quiz', request_poll=KeyboardButtonPollType())
    keyboard_builder.adjust(3, 2, 1)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Choose action:')