from telebot import TeleBot, types
from decouple import config


bot = TeleBot(config('TELEGRAM_TOKEN'))


@bot.message_handler(commands=["start"])
def hello_word(message):
    bot.reply_to(message, "Hello, {}!".format(message.from_user.first_name))


@bot.message_handler(commands=["local", "endereco"])
def local_botoes(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(types.InlineKeyboardButton(
        text="Tutoriais e Sprints",
        callback_data="local_tutoriais_sprints"
    ))
    keyboard.row(types.InlineKeyboardButton(
        text="Palestras",
        callback_data="local_palestras"
    ))
    bot.send_message(message.chat.id, "Para onde você quer ir?", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda callback: callback.data == "local_palestras")
def local_palestras(callback):
    bot.send_message(callback.message.chat.id, (
        "As palestras da *Python Brasil 2019* acontecerão no endereço:\n"
        "Centro de Convenções Ribeirão Preto\n"
        "R. Bernardinho de Campos, 999 - Centro"
    ), parse_mode="markdown")
    bot.send_location(callback.message.chat.id, -21.1748969, -47.8098745)


@bot.callback_query_handler(func=lambda callback: callback.data == "local_tutoriais_sprints")
def local_tutoriais_sprints(callback):
    pass


# @bot.message_handler(commands=["local", "endereco"])
# def local(message):
#     bot.send_message(message.chat.id, (
#         "As palestras da *Python Brasil 2019* acontecerão no endereço:\n"
#         "Centro de Convenções Ribeirão Preto\n"
#         "R. Bernardinho de Campos, 999 - Centro"
#     ), parse_mode="markdown")
#     bot.send_location(message.chat.id, -21.1748969, -47.8098745)


bot.polling()