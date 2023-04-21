import telebot
import csv

CHAVE_API = "6000648389:AAEK0Qh9377tG32QRcuhUvC-AjVuQGgb9jY"

bot = telebot.TeleBot(CHAVE_API)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    with open('data/alunos.csv', 'r', newline='') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            if mensagem.text in linha[1]:
                bot.reply_to(mensagem, 'Sua presença foi registrada! :)')
                break
        else:
            bot.reply_to(mensagem, 'Sua presença não foi registrada... :(')
bot.polling()

