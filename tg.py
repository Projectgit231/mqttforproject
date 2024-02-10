import telebot
import groups


token = ''

bot = telebot.TeleBot(token)


class tgsendmessage:
    def __init__(id):
        #Отправление сообщения родителю/преподавателю о приходе студента в техникум
        if id not in groups.subscribed: return

        message = groups[id]["firsName"] + " пришёл в техникум." 
        for chatid in groups.subscribed[id]:
            bot.reply_text(chatid, message)


class tgsubscribe:
    def __init__(subscribe, id, chatid):
        if subscribe: 
            if id[chatid] not in groups.subscribed[id]: groups.subscribed[id].append(chatid)            
            return
        if id[chatid] in groups.subscribed[id]: groups.subscribed[id].remove(chatid)
