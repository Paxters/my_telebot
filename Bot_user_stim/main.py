from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup,CallbackQuery
import logging
import random

TOKEN = '6024101388:AAFouG_DemjX8AZjn57aJJKBas0SnfCYODc'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.ERROR) 

rand = random.randint(1111111111,9999999999)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    kb = [
    [
    types.KeyboardButton(text="🤓О нас", resize_keyboard=True),
    types.KeyboardButton(text="Atomic Heart", resize_keyboard=True)
    ],
    [
    types.KeyboardButton(text="Игры", resize_keyboard=True),
    types.KeyboardButton(text="Ключи", resize_keyboard=True)
    ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
    await message.reply('Напиши мне что нибудь', reply_markup=keyboard)


@dp.message_handler(Text(equals="Atomic Heart"))
async def test(message: types.Message):
    kbs = [
    [types.KeyboardButton(text="Главные Герои", resize_keyboard=True)],

    [types.KeyboardButton(text="Ежиха", resize_keyboard=True),
    types.KeyboardButton(text="Беляш", resize_keyboard=True)
    ],

    [types.KeyboardButton(text="ВОВЧИК «ЛАБОРАНТ»", resize_keyboard=True),
    types.KeyboardButton(text="Плющ", resize_keyboard=True)],

    [types.KeyboardButton(text="Блезняшки", resize_keyboard=True),
    types.KeyboardButton(text="НА-Т256 «НАТАША»", resize_keyboard=True)],

    [types.KeyboardButton(text="РОСА", resize_keyboard=True),
    types.KeyboardButton(text="КРУПНЫЙ КУЛТЫШ", resize_keyboard=True)
    ],
    [
        types.KeyboardButton(text="Назад", resize_keyboard=True)
    ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kbs, resize_keyboard=True, one_time_keyboard=True)
    await message.reply('Выберите или напишите что нибудь', reply_markup=keyboard)


@dp.message_handler(Text(equals="Ежиха"))
async def esjikha(message: types.Message):
    kbss = [
    [types.KeyboardButton(text="Видео-обзор", resize_keyboard=True),
    types.KeyboardButton(text="Назад", resize_keyboard=True)]
    ]
    photo = "https://images.stopgame.ru/uploads/users/2020/583766/00038.HhjJdVe.png"
    await message.reply(f"<b>Босс Ежиха</b>\nсложность босса ⭐️⭐️⭐️\n3/5\n<i>Босс представляет собой большой стальной шар, созданный для проекта коллектив, с помощью его можно было быстро сеять поля, на самом деле версий применеий данного робота очень много.</i>\n<b>Способности босса:</b>\nСверх-прыжок\nАтакующая волна\n<b>Ресурсы после победы:</b>\nэнергомодуль (х2);нейромодуль;нейрополимер (х48);микроэлектроника (х3);химия (х3);детали из металла (х25);синтетический материал (х10)", parse_mode="HTML")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    keyboard = types.ReplyKeyboardMarkup(keyboard=kbss, resize_keyboard=True, one_time_keyboard=True)
    await message.reply('Вернуться назад?', reply_markup=keyboard)



@dp.message_handler(Text(equals="Назад"))
async def back_to_start(message: types.Message):
    await message.answer("Вы вернулись в начало.")
    kb = [
    [
    types.KeyboardButton(text="🤓О нас", resize_keyboard=True),
    types.KeyboardButton(text="Atomic Heart", resize_keyboard=True)
    ],
    [
    types.KeyboardButton(text="Игры", resize_keyboard=True),
    types.KeyboardButton(text="Ключи", resize_keyboard=True)
    ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
    await message.reply('Выберите или напишите что нибудь', reply_markup=keyboard)


@dp.message_handler(Text(equals="Беляш"))
async def esjikha(message: types.Message):
    kbss = [
    [types.KeyboardButton(text="Видео-обзор", resize_keyboard=True),
    types.KeyboardButton(text="Назад", resize_keyboard=True)]
    ]
    photo = "https://wotpack.ru/wp-content/uploads/2023/02/6-29.jpg"
    await message.reply(f"<b>Беляш</b>\nСложность босса⭐️⭐️⭐️\n3/5\n<i>МА-9 «Беляш» — босс, преграждающий вход в театр. Несмотря на устрашающие габариты, рассматриваемого противника можно назвать одним из слабейших в сравнении с теми, что представлены в игре. Его анимации медлительны и предсказуемы, отчего легко предугадать, в какой момент стоит уклониться. Однако, несмотря на низкую сложность, Беляш способен похвастаться сопротивлением к стихийному урону. Его единственная уязвимость — взрывоопасное вооружение. Используйте его вместе с ШОКом, чтобы как можно быстрее разобраться с «жирной» машиной.</i>\n<b>Награда за победу</b>\nмикроэлектроника (х5);\n детали из металла (х25);\nсинтетический материал (х5);\nнейрополимер (х69); ", parse_mode="HTML")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    keyboard = types.ReplyKeyboardMarkup(keyboard=kbss, resize_keyboard=True, one_time_keyboard=True)
    await message.reply('Напиши мне что нибудь', reply_markup=keyboard)




@dp.message_handler(Text(equals="ВОВЧИК «ЛАБОРАНТ»"))
async def esjikha(message: types.Message):
        kbss = [
        [types.KeyboardButton(text="Видео-обзор", resize_keyboard=True),
        types.KeyboardButton(text="Назад", resize_keyboard=True)]
        ]
        photo = "https://wotpack.ru/wp-content/uploads/2023/02/21-10.jpg"
        await message.reply(f"<b>Черный-Вовчик</b>\nСложность босса⭐️\n1/5\n<i>Вовчик - это самый первый и легкий босс. По истории вселенной, Вовчик обычный(белый), выполняет функцию Мастера на все руки, а всех моделей, которые себя более жестоко ведут, принято в одевать в черный цвет оболочки.</i>\n<b>Награда за победу</b>\nмикроэлектроника (х5);\n детали из металла (х5);\nсинтетический материал (х5);\nнейрополимер (х10);", parse_mode="HTML")
        await bot.send_photo(chat_id=message.from_user.id, photo=photo)
        keyboard = types.ReplyKeyboardMarkup(keyboard=kbss, resize_keyboard=True, one_time_keyboard=True)
        await message.reply('Вернуться назад?', reply_markup=keyboard)




@dp.message_handler(Text(equals="Плющ"))
async def esjikha(message: types.Message):
        kbss = [
        [types.KeyboardButton(text="Видео-обзор", resize_keyboard=True),
        types.KeyboardButton(text="Назад", resize_keyboard=True)]
        ]
        photo = "https://wotpack.ru/wp-content/uploads/2023/03/Boss-Pljushh.jpg"
        await message.reply(f"<b>Плющ</b>\nСложность босса⭐️⭐️⭐️⭐️\n4/5\n<i>Плющ - Можно сказать самый первый сложный босс в игре. Плющ - это неудачный эксперемент внедрения красного нейрополимера в человека. Кстати факт, Харитон Захарович умер из-за этого нейрополимера</i>\n<b>Награда за победу</b>\nсинтетический материал (х6);\nнейрополимер (х35);", parse_mode="HTML")
        await bot.send_photo(chat_id=message.from_user.id, photo=photo)
        keyboard = types.ReplyKeyboardMarkup(keyboard=kbss, resize_keyboard=True, one_time_keyboard=True)
        await message.reply('Вернуться назад?', reply_markup=keyboard)




@dp.message_handler(Text(equals="Блезняшки"))
async def esjikha(message: types.Message):
        kbss = [
        [types.KeyboardButton(text="Видео-обзор", resize_keyboard=True),
        types.KeyboardButton(text="Назад", resize_keyboard=True)]
        ]
        photo = "https://news.store.rambler.ru/img/2f5f43a3f95e6be0be87a464009ef919?img-format=auto&img-1-resize=height:710"
        await message.reply(f"<b>Блезняшки</b>\nСложность босса⭐️⭐️⭐️⭐️⭐️\n5/5\n<i>Блезняшки - это самые трудные боссы в игре. По сюжету, это личные телохранители академика Сеченого, в конце игры оказывается, что две эти блезняшки - это жена Майора Нечаева...</i>\n<b>Награда за победу</b>\nНаграды не пологается.", parse_mode="HTML")
        await bot.send_photo(chat_id=message.from_user.id, photo=photo)
        keyboard = types.ReplyKeyboardMarkup(keyboard=kbss, resize_keyboard=True, one_time_keyboard=True)
        await message.reply('Вернуться назад?', reply_markup=keyboard)



@dp.message_handler(Text(equals="НА-Т256 «НАТАША»"))
async def esjikha(message: types.Message):
    kbss = [
    [types.KeyboardButton(text="Видео-обзор", resize_keyboard=True),
    types.KeyboardButton(text="Назад", resize_keyboard=True)]
    ]
    photo = "https://rampaga.ru/_sf/287/90040043.jpg"
    await message.reply(f"<b>Наташа</b>\nСложность босса⭐⭐⭐\n1/5\n<i>НА-Т256 «Наташа» — настоящий танк. Огромные габариты этого робота делают относительно небольшую арену, где проходит сражение с боссом, еще меньше. К счастью, машина медленнее большинства противников: уклоняться от ее физических атак несложно. Главное, приноровиться к огненному залпу, которым Наташа время от времени окатывает майора Нечаева.</i>\n<b>Награда за победу</b>\nмикроэлектроника (х3);\n детали из металла (х25);\nнейрополимер (х56);", parse_mode="HTML")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    keyboard = types.ReplyKeyboardMarkup(keyboard=kbss, resize_keyboard=True, one_time_keyboard=True)
    await message.reply('Вернуться назад?', reply_markup=keyboard)



@dp.message_handler(Text(equals="РОСА"))
async def esjikha(message: types.Message):
    kbss = [
    [types.KeyboardButton(text="Видео-обзор", resize_keyboard=True),
    types.KeyboardButton(text="Назад", resize_keyboard=True)]
    ]
    photo = "https://i.ytimg.com/vi/dM9jaQVDx2g/maxresdefault.jpg"
    await message.reply(f"<b>Роса</b>\nСложность босса⭐⭐⭐\n3/5\n<i>РОСА — большой и маневренный противник. Если в инвентаре майора Нечаева до сих пор отсутствует прокаченный «Крепыш», самое время это исправить. Причина проста — только названное оружие может обеспечить быструю победу над монстром, который устойчив ко многим типам вооружения, а также имеет высокое сопротивление к стихийному урону.</i>\n<b>Награда за победу</b>\nмикроэлектроника (х5);\n детали из металла (х25);\nсинтетический материал (х9);\nнейрополимер (х52);", parse_mode="HTML")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    keyboard = types.ReplyKeyboardMarkup(keyboard=kbss, resize_keyboard=True, one_time_keyboard=True)
    await message.reply('Вернуться назад?', reply_markup=keyboard)


@dp.message_handler(Text(equals="КРУПНЫЙ КУЛТЫШ"))
async def esjikha(message: types.Message):
    kbss = [
    [types.KeyboardButton(text="Видео-обзор", resize_keyboard=True),
    types.KeyboardButton(text="Назад", resize_keyboard=True)]
    ]
    photo = "https://wotpack.ru/wp-content/uploads/2023/02/4-34.jpg"
    await message.reply(f"<b>Крупный Култыш</b>\nСложность босса⭐\n1/5\n<i>Крупный Култыш считается мини-боссом, несмотря на возможные трудности, которые могут появится в процессе сражения с монстром. Причина заключается в том, что после его убийства у майора Нечаева не получится поживиться достаточным количеством расходных материалов (в сравнении с другими противниками, рассмотренными в статье). Помимо этого, враг негабаритен, что упрощает сражение с ним в узком пространстве.</i>\n<b>Награда за победу</b>\nмикроэлектроника (х5);\n детали из металла (х5);\nсинтетический материал (х5);\nнейрополимер (х10);", parse_mode="HTML")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    keyboard = types.ReplyKeyboardMarkup(keyboard=kbss, resize_keyboard=True, one_time_keyboard=True)
    await message.reply('Вернуться назад?', reply_markup=keyboard)

@dp.message_handler(Text(equals="Главные Герои"))
async def GG(message: types.Message):
    await message.answer("Вы попали в раздел Главные Герои")
    kb = [
    [
    types.KeyboardButton(text="Майор Нечаев", resize_keyboard=True),
    types.KeyboardButton(text="ХРАЗ", resize_keyboard=True)
    ],
    [
    types.KeyboardButton(text="Академик Сеченов", resize_keyboard=True),
    types.KeyboardButton(text="Назад", resize_keyboard=True)
    ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
    await message.reply('Выберите или напишите что нибудь', reply_markup=keyboard)


@dp.message_handler(Text(equals="Майор Нечаев"))
async def esjikha(message: types.Message):
    kbss = [
    [
    types.KeyboardButton(text="Назад", resize_keyboard=True)]
    ]
    photo = "https://images.stopgame.ru/uploads/users/2021/519457/00212.PJ8ic90.jpg"
    await message.reply(f"<b>Майор Нечаев</b> <i>Нечаев Сергей Алексеевич, он же П-3 (произн. пэ-три) — офицер разведки по особым поручениям и специалист по урегулированию сложных ситуаций любыми, в том числе силовыми методами. Находится в подчинении у товарища Сеченова. Сотрудник предприятия «3826».</i>", parse_mode="HTML")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    keyboard = types.ReplyKeyboardMarkup(keyboard=kbss, resize_keyboard=True, one_time_keyboard=True)
    await message.reply('Вернуться назад?', reply_markup=keyboard)

@dp.message_handler(Text(equals="ХРАЗ"))
async def esjikha(message: types.Message):
    kbss = [
    [
    types.KeyboardButton(text="Назад", resize_keyboard=True)]
    ]
    photo = "https://i.playground.ru/p/7OstDRwMjJvfymxCihs20w.jpeg"
    await message.reply(f"<b>ХРАЗ - Харитон</b><i>ХРАЗ (ХРАнитель Знаний) или же Харитон Захаров Радеонович — полимерный искусственный интеллект встроенный в экспериментальную силовую перчатку, обладающий обширным запасом знаний, которыми он пользуется давая Майору Нечаеву советы во время битвы.</i>", parse_mode="HTML")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    keyboard = types.ReplyKeyboardMarkup(keyboard=kbss, resize_keyboard=True, one_time_keyboard=True)
    await message.reply('Вернуться назад?', reply_markup=keyboard)


@dp.message_handler(Text(equals="Академик Сеченов"))
async def esjikha(message: types.Message):
    kbss = [
    [
    types.KeyboardButton(text="Назад", resize_keyboard=True)]
    ]
    photo = "https://i.ytimg.com/vi/L_4jVjQiCQM/maxresdefault.jpg"
    await message.reply(f"<b>Академик Сеченов</b><i>Дмитрий Сеченов из Atomic Heart является одним из ключевых персонажей игры, будучи директором и ведущим изобретателем Предприятия 3826. По совместительству занимает почетный пост министра промышленности. Именно за Сеченовым стоит изобретение нейрополимеров и нейросети Коллектив 1.0 и Коллектив 2.0.</i>", parse_mode="HTML")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    keyboard = types.ReplyKeyboardMarkup(keyboard=kbss, resize_keyboard=True, one_time_keyboard=True)
    await message.reply('Вернуться назад?', reply_markup=keyboard)



@dp.message_handler(Text(equals="🤓О нас"))
async def esjikha(message: types.Message):
     markup = types.InlineKeyboardMarkup()
     sozdat = types.InlineKeyboardButton("Наш Канал", url="https://www.youtube.com/channel/UCAdlW9OUi0_ORiaYPalkkCA")
     kollege = types.InlineKeyboardButton("Сайт колледжа", url="https://nogkolledzh.ru")
     markup.row(sozdat, kollege)
     await message.reply(f'Мы компания, которая занимается продажей игр в Стим💸\nТак же в нашем боте можно узнать о Atomic Heart💗\n<b>У нас в наличии более 700+ ключей с разными играми по самым низким ценам на рынке!💦</b>.', reply_markup=markup, parse_mode="HTML")

@dp.message_handler(Text(equals="Ключи"))
async def GG(message: types.Message):
    await message.answer("Вы попали в раздел Ключи")
    kb = [
    [
    types.KeyboardButton(text="Steam", resize_keyboard=True),
    types.KeyboardButton(text="Epic Games", resize_keyboard=True)
    ],
    [
    types.KeyboardButton(text="Origin", resize_keyboard=True),
    ],
    [
        types.KeyboardButton(text="Назад", resize_keyboard=True)
    ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
    await message.reply('Выберите или напишите что нибудь', reply_markup=keyboard)

@dp.message_handler(Text(equals="Steam"))
async def GG(message: types.Message):
    await message.answer("Вы попали в раздел Steam, выберите игру которую хотите купить:")
    kb = [
    [
    types.KeyboardButton(text="GTA5", resize_keyboard=True),
    types.KeyboardButton(text="Rainbow 6", resize_keyboard=True)
    ],

    [
    types.KeyboardButton(text="Atomic Hearts", resize_keyboard=True),
    types.KeyboardButton(text="City car driving", resize_keyboard=True)
    ],
    [
    types.KeyboardButton(text="RUST", resize_keyboard=True),
    types.KeyboardButton(text="Squad", resize_keyboard=True)
    ],
    [
    types.KeyboardButton(text="Назад", resize_keyboard=True)
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
    await message.reply('Выберите или напишите что нибудь', reply_markup=keyboard)

@dp.message_handler(Text(equals="Epic Games"))
async def GG(message: types.Message):
    await message.answer("Вы попали в раздел Epic Games, выберите игру которую хотите купить:")
    kb = [
    [
    types.KeyboardButton(text="GTA5", resize_keyboard=True),
    types.KeyboardButton(text="Hitman 3", resize_keyboard=True)
    ],

    [
    types.KeyboardButton(text="Fortnite", resize_keyboard=True),
    types.KeyboardButton(text="Mafia 3", resize_keyboard=True)
    ],
    [
    types.KeyboardButton(text="Назад", resize_keyboard=True)
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
    await message.reply('Выберите или напишите что нибудь', reply_markup=keyboard)

@dp.message_handler(Text(equals="Origin"))
async def GG(message: types.Message):
    await message.answer("Вы попали в раздел Origin, выберите игру которую хотите купить:")
    kb = [
    [
    types.KeyboardButton(text="Call of Duty Modern", resize_keyboard=True),
    types.KeyboardButton(text="Hitman 3", resize_keyboard=True)
    ],

    [
    types.KeyboardButton(text="Assasin`s Creed", resize_keyboard=True),
    types.KeyboardButton(text="Battlefield 2042", resize_keyboard=True)
    ],
    [
    types.KeyboardButton(text="Назад", resize_keyboard=True)
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
    await message.reply('Выберите или напишите что нибудь', reply_markup=keyboard)



@dp.message_handler(Text(equals='GTA5', ignore_case=True))
async def cmd_gta5(message: types.Message):
    await message.reply('Вы выбрали GTA5, её стоимость 699 рублей!✅')
    photo = "https://wallpapercave.com/wp/wp2880216.jpg"
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    kbc = [
    [
    types.KeyboardButton(text="Купить", resize_keyboard=True),
    types.KeyboardButton(text="Проверить покупку", resize_keyboard=True)
    ],
    [
    types.KeyboardButton(text="Назад", resize_keyboard=True)
    ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kbc, resize_keyboard=True)
    await message.reply('Выберите или напишите что нибудь', reply_markup=keyboard)

@dp.message_handler(Text(equals='Rainbow 6', ignore_case=True))
async def cmd_gta5(message: types.Message):
    await message.reply('Вы выбрали Rainbow 6, её стоимость 399 рублей!✅')
    photo = "https://cdn.windowsreport.com/wp-content/uploads/2020/06/Rainbow-Six-Siege-packet-loss.jpg"
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    kbc = [
    [
    types.KeyboardButton(text="Купить", resize_keyboard=True),
    types.KeyboardButton(text="Проверить покупку", resize_keyboard=True)
    ],
    [
    types.KeyboardButton(text="Назад", resize_keyboard=True)
    ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kbc, resize_keyboard=True)
    await message.reply('Выберите или напишите что нибудь', reply_markup=keyboard)



@dp.message_handler(Text(equals='Atomic Hearts', ignore_case=True))
async def cmd_gta5(message: types.Message):
    await message.reply('Вы выбрали Atomic Heart, её стоимость 899 рублей!✅')
    photo = "https://i.ytimg.com/vi/HfLxZEW8KLI/maxresdefault.jpg"
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    kbc = [
    [
    types.KeyboardButton(text="Купить", resize_keyboard=True),
    types.KeyboardButton(text="Проверить покупку", resize_keyboard=True)
    ],
    [
    types.KeyboardButton(text="Назад", resize_keyboard=True)
    ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kbc, resize_keyboard=True)
    await message.reply('Выберите или напишите что нибудь', reply_markup=keyboard)


@dp.message_handler(Text(equals='City car driving', ignore_case=True))
async def cmd_gta5(message: types.Message):
    await message.reply('Вы выбрали City car driving, её стоимость 99 рублей!✅')
    photo = "https://i.ytimg.com/vi/OBhl2syBUK4/maxresdefault.jpg"
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    kbc = [
    [
    types.KeyboardButton(text="Купить", resize_keyboard=True),
    types.KeyboardButton(text="Проверить покупку", resize_keyboard=True)
    ],
    [
    types.KeyboardButton(text="Назад", resize_keyboard=True)
    ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kbc, resize_keyboard=True)
    await message.reply('Выберите или напишите что нибудь', reply_markup=keyboard)

@dp.message_handler(Text(equals='RUST', ignore_case=True))
async def cmd_gta5(message: types.Message):
    await message.reply('Вы выбрали RUST, её стоимость 799 рублей!❌')
    photo = "https://i.ytimg.com/vi/AgazXWQH-gQ/maxresdefault.jpg?7857057827"
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    kbc = [
    [
    types.KeyboardButton(text="Купить", resize_keyboard=True),
    types.KeyboardButton(text="Проверить покупку", resize_keyboard=True)
    ],
    [
    types.KeyboardButton(text="Назад", resize_keyboard=True)
    ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kbc, resize_keyboard=True)
    await message.reply('Выберите или напишите что нибудь', reply_markup=keyboard)

@dp.message_handler(Text(equals='Squad', ignore_case=True))
async def cmd_gta5(message: types.Message):
    await message.reply('Вы выбрали Squad, её стоимость 399 рублей!✅')
    photo = "https://pic.rutubelist.ru/video/b9/4f/b94f97da23948bbe4e988c88c2067b9e.jpg"
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    kbc = [
    [
    types.KeyboardButton(text="Купить", resize_keyboard=True),
    types.KeyboardButton(text="Проверить покупку", resize_keyboard=True)
    ],
    [
    types.KeyboardButton(text="Назад", resize_keyboard=True)
    ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kbc, resize_keyboard=True)
    await message.reply('Выберите или напишите что нибудь', reply_markup=keyboard)

@dp.message_handler(Text(equals='Fortnite', ignore_case=True))
async def cmd_gta5(message: types.Message):
    await message.reply('Вы выбрали Fortnite, она бесплатная, но вы можете купить код за 299 рублей!✅')
    photo = "https://www.digiseller.ru/preview/876706/p1_3267009_21517a64.jpg"
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    kbc = [
    [
    types.KeyboardButton(text="Купить", resize_keyboard=True),
    types.KeyboardButton(text="Проверить покупку", resize_keyboard=True)
    ],
    [
    types.KeyboardButton(text="Назад", resize_keyboard=True)
    ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kbc, resize_keyboard=True)
    await message.reply('Выберите или напишите что нибудь', reply_markup=keyboard)


@dp.message_handler(Text(equals='Mafia 3', ignore_case=True))
async def cmd_gta5(message: types.Message):
    await message.reply('Вы выбрали Mafia 3, её стоимость 199 рублей!✅')
    photo = "https://i.playground.ru/p/xvIlt7TwKMwLQmm74tRFrA.jpeg"
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    kbc = [
    [
    types.KeyboardButton(text="Купить", resize_keyboard=True),
    types.KeyboardButton(text="Проверить покупку", resize_keyboard=True)
    ],
    [
    types.KeyboardButton(text="Назад", resize_keyboard=True)
    ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kbc, resize_keyboard=True)
    await message.reply('Выберите или напишите что нибудь', reply_markup=keyboard)


@dp.message_handler(Text(equals='Hitman 3', ignore_case=True))
async def cmd_gta5(message: types.Message):
    await message.reply('Вы выбрали Hitman 3, её стоимость 299 рублей!✅')
    photo = "https://graph.digiseller.ru/img.ashx?idd=3558072"
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    kbc = [
    [
    types.KeyboardButton(text="Купить", resize_keyboard=True),
    types.KeyboardButton(text="Проверить покупку", resize_keyboard=True)
    ],
    [
    types.KeyboardButton(text="Назад", resize_keyboard=True)
    ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kbc, resize_keyboard=True)
    await message.reply('Выберите или напишите что нибудь', reply_markup=keyboard)


@dp.message_handler(Text(equals='Call of Duty Modern', ignore_case=True))
async def cmd_gta5(message: types.Message):
    await message.reply('Вы выбрали Call of Duty Modern, её стоимость 99 рублей!❌')
    photo = "https://difmark.com/images/product/9/7/79737/call-of-duty-modern-warfare-ii-2022-ps4_orig_2.jpg"
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    kbc = [
    [
    types.KeyboardButton(text="Купить", resize_keyboard=True),
    types.KeyboardButton(text="Проверить покупку", resize_keyboard=True)
    ],
    [
    types.KeyboardButton(text="Назад", resize_keyboard=True)
    ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kbc, resize_keyboard=True)
    await message.reply('Выберите или напишите что нибудь', reply_markup=keyboard)

@dp.message_handler(Text(equals='Assasin`s Creed', ignore_case=True))
async def cmd_gta5(message: types.Message):
    await message.reply('Вы выбрали все части Assasin`s Creed, её стоимость 59 рублей!❌')
    photo = "https://wallpaper-mania.com/wp-content/uploads/2018/09/High_resolution_wallpaper_background_ID_77700789544.jpg"
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    kbc = [
    [
    types.KeyboardButton(text="Купить", resize_keyboard=True),
    types.KeyboardButton(text="Проверить покупку", resize_keyboard=True)
    ],
    [
    types.KeyboardButton(text="Назад", resize_keyboard=True)
    ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kbc, resize_keyboard=True)
    await message.reply('Выберите или напишите что нибудь', reply_markup=keyboard)

@dp.message_handler(Text(equals='Battlefield 2042', ignore_case=True))
async def cmd_gta5(message: types.Message):
    await message.reply('Вы выбрали Battlefield 2042, её стоимость 359 рублей!✅')
    photo = "https://graph.digiseller.ru/img.ashx?idd=3611953"
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    kbc = [
    [
    types.KeyboardButton(text="Купить", resize_keyboard=True),
    types.KeyboardButton(text="Проверить покупку", resize_keyboard=True)
    ],
    [
    types.KeyboardButton(text="Назад", resize_keyboard=True)
    ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kbc, resize_keyboard=True)
    await message.reply('Выберите или напишите что нибудь', reply_markup=keyboard)


@dp.message_handler(Text(equals='Игры'))
async def buy(message: types.Message):
    await message.reply(f'проверка игры на наличие:\n<b>Steam</b>\nGTA5✅\nRainbow 6✅\nAtomic Hearts✅\nCity car driving✅\nRUST❌\nSquad✅\n<b>Epic Games</b>\nFortnite✅\nMafia 3✅\nHitman 3✅\n<b>Origin</b>\nCall of Duty Modern✅\nHitman 3✅\nAsassin`s Creed❌\nBattlefield 2042✅', parse_mode="HTML")


@dp.message_handler(Text(equals='Купить'))
async def buy(message: types.Message):
    await message.reply(f'Вот ссылка на оплату!\nhttps://qiwi.com')

@dp.message_handler(Text(equals='Видео-обзор'))
async def buy(message: types.Message):
    await message.reply(f'Смотри все босс-файты!!\nhttps://www.youtube.com/watch?v=CBiriwlic78')

@dp.message_handler(Text(equals="Проверить покупку"))
async def BUY(message: types.Message):
     await message.reply('Покупка проверяется...')
     await message.reply(f'Оплата Успешная!✅\nВот ваш ключ {rand}! Спасибо за покупку!\nПосле покупки нажмите (Назад)')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)