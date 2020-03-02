import telebot
import xkcd

API_TOKEN = '<api_token>'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(func=lambda message: True)
def process_query(message):
    if message.text == 'xkcd':
        random_comic = xkcd.getRandomComic()
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(telebot.types.KeyboardButton('Check out another xkcd comic!'))
        bot.send_photo(message.chat.id, random_comic.getImageLink(), caption='*' +
                       random_comic.getTitle() + '*\n' + random_comic.getAltText() +
                       '\n' + random_comic.getExplanation(), parse_mode='Markdown',
                       reply_to_message_id=message.message_id, reply_markup=markup)
    else:
        bot.reply_to(message, message.text)


bot.polling()
