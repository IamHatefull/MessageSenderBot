from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

select_macbook = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Macbook Air 13" M1 2020',
            callback_data='apple_air_13_m1_2020'
        )
    ],
    [
        InlineKeyboardButton(
            text='Macbook Air 13" M1 2020',
            callback_data='apple_air_13_m1_2020'
        )
    ],
    [
        InlineKeyboardButton(
            text='Macbook Pro 14" M1 Pro 2021',
            callback_data='apple_pro_14_m1_2021'
        )
    ],
    [
        InlineKeyboardButton(
            text='Macbook Pro 16" M1 2019',
            callback_data='apple_pro_16_i7_2019'
        )
    ],
    [
        InlineKeyboardButton(
            text='Link',
            callback_data='https://google.com'
        )
    ],
    [
        InlineKeyboardButton(
            text='Profile',
            callback_data='tg://user?id=66089851'
        )
    ]
])