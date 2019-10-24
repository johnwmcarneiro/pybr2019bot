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


@bot.callback_query_handler(func=lambda callback: callback.data in ["local_palestras", "local_tutoriais_sprints"])
def local_enderecos(callback):
    if callback.data == "local_palestras":
        message = (
            "As palestras da *Python Brasil 2019* acontecerão no endereço:\n"
            "Centro de Convenções Ribeirão Preto\n"
            "R. Bernardinho de Campos, 999 - Centro"
        )
        latitude = -21.1748969
        longitude = -47.8098745
    else:
        message = (
            "Os tutoriais e sprints da *Python Brasil 2019* acontecerão no endereço:\n"
            "Estácio Centro Universitário\n"
            "Rua Abrahão Issa Halach, 980 - Ribeirânia, Ribeirão Preto - SP, 14096-160"
        )
        latitude = -21.1929639
        longitude =  -47.8174115

    bot.edit_message_text(message,
        callback.message.chat.id,
        callback.message.message_id,
        parse_mode="markdown"
    )
    bot.send_location(callback.message.chat.id, latitude, longitude)


bot.polling()