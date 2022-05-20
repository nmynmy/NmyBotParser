import datetime
import os
import random
import sqlite3
import string
import subprocess
import time

from telebot import types

import telebot
from xlsxwriter.workbook import Workbook

bot = telebot.TeleBot('5183755894:AAFJWAW0Xf3Vw5X2RLe-tJvqOBI1OKbZmjE')
def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string
def generate_xlsx(name_file,date):
    workbook = Workbook(name_file)
    worksheet = workbook.add_worksheet()
    conn = sqlite3.connect('IDGos.db')
    c = conn.cursor()
    #c.execute("select * from IDSGOS")
    mysel = c.execute("select * from IDSGOS  where Дата = '"+date+"'")

    for i, description in enumerate(mysel.description):
        worksheet.write(0, i, description[0])
        worksheet.set_column(i,i,27)
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i+1, j, value)
    workbook.close()
    conn.commit()

def generate_xlsxOneFile(name_file,dates):
    workbook = Workbook(name_file)
    worksheet = workbook.add_worksheet()
    conn = sqlite3.connect('IDGos.db')
    c = conn.cursor()
    #c.execute("select * from IDSGOS")
    mysel = c.execute("select * from IDSGOS  where Дата = '15.04.2022'")
    for i, description in enumerate(mysel.description):
        worksheet.write(0, i, description[0])
        worksheet.set_column(i, i, 27)
    last=1
    conn.commit()
    conn = sqlite3.connect('IDGos.db')
    c = conn.cursor()
    for date in dates:
        mysel1 = c.execute("select * from IDSGOS  where Дата = '" + date + "'")
        for i, row in enumerate(mysel1):
            for j, value in enumerate(row):
                worksheet.write(i+last, j, value)
        if i==0:
            last += 1
        else:
            last+=i
    workbook.close()
    conn.commit()
def Today_get(userid):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("За сегодня")
    item2 = types.KeyboardButton("За прошлые 7 дней")
    item4 = types.KeyboardButton("За прошлые 14 дней")
    item5 = types.KeyboardButton("За прошлые 30 дней")
    item3 = types.KeyboardButton("Запустить парсинг")
    markup.add(item1)
    markup.add(item2)
    markup.add(item4)
    markup.add(item5)
    markup.add(item3)
    A = datetime.datetime.today()
    date = A.strftime("%d.%m.%Y")
    #date = '10.04.2022'

    namefile=date+"_"+generate_random_string(8)+".xlsx"
    namefileBot="Файл за "+date
    generate_xlsx(namefile,date)
    with open(namefile, "rb") as misc:
        bot.send_document(userid,misc,caption=namefileBot,reply_markup=markup)
    os.remove(namefile)

def Week_get(userid):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("За сегодня")
    item2 = types.KeyboardButton("За прошлые 7 дней")
    item4 = types.KeyboardButton("За прошлые 14 дней")
    item5 = types.KeyboardButton("За прошлые 30 дней")
    item3 = types.KeyboardButton("Запустить парсинг")
    markup.add(item1)
    markup.add(item2)
    markup.add(item4)
    markup.add(item5)
    markup.add(item3)
    dates = []
    for b in range(1,8):
        today = datetime.date.today()
        week_ago = today - datetime.timedelta(days=b)
        date = week_ago.strftime("%d.%m.%Y")
        dates.append(date)
    for date in dates:
        namefile = generate_random_string(16) + ".xlsx"
        namefileBot = "Файл за " + date
        generate_xlsx(namefile, date)
        with open(namefile, "rb") as misc:
            bot.send_document(userid, misc, caption=namefileBot, reply_markup=markup)
        os.remove(namefile)

def Week_get_onefile(userid):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("За сегодня")
    item2 = types.KeyboardButton("За прошлые 7 дней")
    item4 = types.KeyboardButton("За прошлые 14 дней")
    item5 = types.KeyboardButton("За прошлые 30 дней")
    item3 = types.KeyboardButton("Запустить парсинг")
    markup.add(item1)
    markup.add(item2)
    markup.add(item4)
    markup.add(item5)
    markup.add(item3)
    dates = []
    for b in range(1,8):
        today = datetime.date.today()
        week_ago = today - datetime.timedelta(days=b)
        date = week_ago.strftime("%d.%m.%Y")
        dates.append(date)

    namefile = dates[-1]+"-"+dates[0]+"_"+generate_random_string(8) + ".xlsx"
    namefileBot = "Файл за " + dates[-1]+"-"+dates[0]
    generate_xlsxOneFile(namefile, dates)
    with open(namefile, "rb") as misc:
        bot.send_document(userid, misc, caption=namefileBot, reply_markup=markup)
    os.remove(namefile)
def Fourteen_get_onefile(userid):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("За сегодня")
    item2 = types.KeyboardButton("За прошлые 7 дней")
    item4 = types.KeyboardButton("За прошлые 14 дней")
    item5 = types.KeyboardButton("За прошлые 30 дней")
    item3 = types.KeyboardButton("Запустить парсинг")
    markup.add(item1)
    markup.add(item2)
    markup.add(item4)
    markup.add(item5)
    markup.add(item3)
    dates = []
    for b in range(1,15):
        today = datetime.date.today()
        week_ago = today - datetime.timedelta(days=b)
        date = week_ago.strftime("%d.%m.%Y")
        dates.append(date)

    namefile = dates[-1]+"-"+dates[0]+"_"+generate_random_string(8) + ".xlsx"
    namefileBot = "Файл за " + dates[-1]+"-"+dates[0]
    generate_xlsxOneFile(namefile, dates)
    with open(namefile, "rb") as misc:
        bot.send_document(userid, misc, caption=namefileBot, reply_markup=markup)
    os.remove(namefile)
def Thirty_get_onefile(userid):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("За сегодня")
    item2 = types.KeyboardButton("За прошлые 7 дней")
    item4 = types.KeyboardButton("За прошлые 14 дней")
    item5 = types.KeyboardButton("За прошлые 30 дней")
    item3 = types.KeyboardButton("Запустить парсинг")
    markup.add(item1)
    markup.add(item2)
    markup.add(item4)
    markup.add(item5)
    markup.add(item3)
    dates = []
    for b in range(1,31):
        today = datetime.date.today()
        week_ago = today - datetime.timedelta(days=b)
        date = week_ago.strftime("%d.%m.%Y")
        dates.append(date)

    namefile = dates[-1]+"-"+dates[0]+"_"+generate_random_string(8) + ".xlsx"
    namefileBot = "Файл за " + dates[-1]+"-"+dates[0]
    generate_xlsxOneFile(namefile, dates)
    with open(namefile, "rb") as misc:
        bot.send_document(userid, misc, caption=namefileBot, reply_markup=markup)
    os.remove(namefile)

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("За сегодня")
    item2 = types.KeyboardButton("За прошлые 7 дней")
    item3 = types.KeyboardButton("Запустить парсинг")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(m.chat.id, 'Бот запущен',reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("За сегодня")
    item2 = types.KeyboardButton("За прошлые 7 дней")
    item4 = types.KeyboardButton("За прошлые 14 дней")
    item5 = types.KeyboardButton("За прошлые 30 дней")
    item3 = types.KeyboardButton("Запустить парсинг")
    markup.add(item1)
    markup.add(item2)
    markup.add(item4)
    markup.add(item5)
    markup.add(item3)
    markup_7 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("За 7 дней одним файлом")
    item2 = types.KeyboardButton("За 7 дней разными файлами")
    markup_7.add(item1)
    markup_7.add(item2)
    try:
        print("=====================")
        print("User: "+message.chat.username+" | "+message.text.strip())
        print("=====================")
    except:
        print("Ошибка вывода")
        print("=====================")
    if message.text.strip() == 'За сегодня':
        Today_get(message.chat.id)
    if message.text.strip() == 'За прошлые 7 дней':
        bot.send_message(message.chat.id,"Выберите:",reply_markup=markup_7)
    if message.text.strip() == 'За прошлые 14 дней':
        Fourteen_get_onefile(message.chat.id)
    if message.text.strip() == 'За прошлые 30 дней':
        Thirty_get_onefile(message.chat.id)
    if message.text.strip() == 'За 7 дней разными файлами':
        Week_get(message.chat.id)
    if message.text.strip() == 'За 7 дней одним файлом':
        Week_get_onefile(message.chat.id)
    if message.text.strip() == 'Запустить парсинг':
        f = open("parsingstatus.txt", "r", encoding='utf-8')
        status = f.readline()
        if(status=="true"):
            bot.send_message(message.chat.id,"Парсинг уже запущен",reply_markup=markup)
        else:
            subprocess.Popen(['python', 'zakupkiparsing.py', str(message.chat.id)])


while True:
    try:
        bot.polling(none_stop=True, interval=0,timeout=200)
    except:
        time.sleep(10)