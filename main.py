import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я бот, который отвечает на вопросы.\n"
        "Напиши /question и свой вопрос после него.\n"
        "Например: /question Чем заняться, когда скучно?"
    )

@bot.message_handler(commands=['question'])
def handle_question(message):
    question = telebot.util.extract_arguments(message.text)

    answers = {
        'Чем заняться когда скучно?': 'Посмотри телевизор',
        'Чем заняться, когда скучно?': 'Пойди погуляй',
        'Чем заняться, когда скучно': 'Приготовь что-нибудь',
        'Чем заняться когда скучно': 'Посмотри фильм'
    }

    if question in answers:
        bot.send_message(message.chat.id, answers[question])
    else:
        bot.send_message(message.chat.id, "К сожалению, я не знаю ответа на этот вопрос.")

bot.infinity_polling()

    
