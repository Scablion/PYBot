import telebot
import csv
import sqlite3

global usname
global mes


bot = telebot.TeleBot('6352100158:AAEOcJ2HnveoSREWaphKDSZtOwBTer90L8E')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    usname = message.from_user.first_name
    mes = message.text
    con = sqlite3.connect('Bot.db')
    cur = con.cursor()
    cur.execute('''
            CREATE TABLE IF NOT EXISTS Clients(
            id integer primary key autoincrement,
            nickname text,
            message text
            )
            ''')
    cur.execute('INSERT INTO Clients(nickname, message) VALUES (?, ?)', (usname, mes))
    con.commit()
    cur.execute('''select * from Clients''')
    with open("outClient.csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",", lineterminator='\r')
        csv_writer.writerow([i[0] for i in cur.description])
        csv_writer.writerows(cur)



bot.polling(none_stop=True)