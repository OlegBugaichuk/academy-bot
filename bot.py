import telebot

bot = telebot.TeleBot("")

name = ''
surname = ''
age = 0
markup = telebot.types.ReplyKeyboardMarkup()
itembtna = telebot.types.KeyboardButton('Мультики')
itembtnv = telebot.types.KeyboardButton('Ужасы')
itembtnc = telebot.types.KeyboardButton('Комедии')
itembtnd = telebot.types.KeyboardButton('Мелодрамы')
markup.row(itembtna, itembtnv)
markup.row(itembtnc, itembtnd)

@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.send_message(message.from_user.id, ' Привет, как тебя зовут?')
  bot.register_next_step_handler(message, get_name)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.reply_to(message, message.text)
  

def get_name(message):
  global name
  name = message.text
  bot.send_message(message.from_user.id, f'Привет {name}')
  bot.send_message(message.from_user.id, 'Сколько тебе лет?')
  bot.register_next_step_handler(message, get_age)


def get_age(message):
  try:
    if int(message.text) > 18:
      bot.send_message(message.from_user.id, f'Заходи {name}, распологайся!')
      bot.send_message(message.from_user.id, "Выбери комнату, для просмотра", reply_markup=markup)
    else:
      bot.send_message(message.from_user.id, f'Прости {name}, но для тебя доступ закрыт')
  except Exception as e:
    bot.send_message(message.from_user.id, f'Прости {name}, но я не понимаю сколько это, Введи еще раз')
    bot.register_next_step_handler(message, get_age)




bot.polling()
