import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import requests
import json
from static import TELEGRAM_TOKEN



TOKEN = TELEGRAM_TOKEN
URL = 'https://geek-jokes.sameerkumar.website/api?format=json'
bot = telebot.TeleBot(TOKEN)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Hello'))
keyboard.add(KeyboardButton('Шутку!'))

headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "97798c91bamsh683aac8a860fdddp18aee9jsn28e65af5506a",
	"X-RapidAPI-Host": "translate-plus.p.rapidapi.com"
}


def get_joke():
    url = "https://simple-elegant-translation-service.p.rapidapi.com/translate"
    payload = {
        "text":  requests.get(URL).json()['joke'],
        "source": "en",
        "target": "ru"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    return response.json()['translations']['translation']


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет, я - бот!', reply_markup=keyboard)


@bot.message_handler(regexp=r'hello\.*')
def say_message(message):
    bot.send_message(message.chat.id, 'Hello!')


@bot.message_handler(regexp=r'шутку!\.*')
def say_message(message):
    bot.send_message(message.chat.id, get_joke())


bot.infinity_polling()