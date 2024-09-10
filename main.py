from tele import Telebot
from weather import Weather
from food import Food
import sys

def make_it_reable(days_datas):
    lst = []
    j = 0
    index = 0

    days = list(days_datas.keys())
    while j < len(days):
        lst.append(days[j] + ": " + days_datas[days[j]][0]+ ", sıcaklık" + days_datas[days[j]][1] + "°C, nem oranı:%" + days_datas[days[j]][2] + "\n\n")
        if j == len(days_datas) - 1:
            lst.append(days[j] + ": " + days_datas[days[j]][0]+ ", sıcaklık:" + days_datas[days[j]][1] + "°C, nem oranı:%" + days_datas[days[j]][2])
        j += 1
    string = ""
    while index < len(lst):
        string += "☁️"+ lst[index]
        index += 1
    return string

def weatherBot(user_input):
    weatherBot = Weather()
    if (len(user_input) == 1 and user_input[0] == "/havadurumu"):
        weather_datas = weatherBot.getWeather()
        print(weather_datas)
        appened_datas = weatherBot.getAlltogether(weather_datas)
        all_datas = make_it_reable(appened_datas)
        Bot.sendMessage(Bot.chat_id, all_datas)
        Bot.sendMessage(Bot.chat_id, "İstanbul için 7 günlük hava durumu bilgisi")
    elif (len(user_input) == 3 and user_input[0] == "/havadurumu"):
       weatherBot.lang = user_input[1]
       weatherBot.city = user_input[2]
       weather_datas = weatherBot.getWeather()
       if weather_datas["success"] == False:
           Bot.sendMessage(Bot.chat_id, "Lütfen tekrar giriniz istenmeyen giriş!!!")
       else:
            appened_datas = weatherBot.getAlltogether(weather_datas)
            string = make_it_reable(appened_datas)
            Bot.sendMessage(Bot.chat_id, string)
    elif (len(user_input) > 3 and user_input[0] == "/havadurumu"):
        Bot.sendMessage(Bot.chat_id, "Lütfen tekrar giriniz istenmeyen giriş!!!")

def foodBot(user_input):
    foodBot = Food()
    if(len(user_input) == 2 and user_input[0].lower() == "/kalori"):
        foodBot.querry = user_input[1]
        food_datas = foodBot.calories()
        if food_datas["success"] == False:
            Bot.sendMessage(Bot.chat_id, "Lütfen tekrar giriniz istenmeyen giriş!!!")
        else:
            calories = foodBot.process_food_data(food_datas)
            Bot.sendMessage(Bot.chat_id, calories)
    elif (len(user_input) > 2 and user_input[0] == "/kalori"):
        Bot.sendMessage(Bot.chat_id, "Lütfen tekrar giriniz istenmeyen giriş!!!")

def helper(user_input):
    if (user_input[0] == "/help"):
        message = instructions_message = (
        "Ben bir yardımcı asistanım\n\n"
        "Herhangi Bir şehirdeki hava durumu koşullarını öğrenmek isterseniz, lütfen şu komutu yazın:\n\n"
        "\"/havadurumu\" [istenilen dil: örn. en, tr, fr] [istediğiniz şehir: örn. İstanbul, Paris]\n\n"
        "Ayrıca, belirli bir yiyeceğin kalorilerini öğrenmek için ise:\n\n"
        "\"/kalori\" [istenilen yiyecek] \n\n"
        "Beni kapatmanız için ise /exit yazmanız yeterli")
        Bot.sendMessage(Bot.chat_id, message)
    elif (user_input[0] != "/help" and user_input[0] != "/havadurumu" and user_input[0] != "/kalori"):
        message = ("bilinmeyen bir komut girdiniz yardım için \"/help\" yazmanız yeterli")
        Bot.sendMessage(Bot.chat_id, message)

if __name__ == "__main__":
    Bot = #Token number
    welcome_message = (
    "🌟 Telebot Sistemi'ne Hoşgeldiniz! 🌟\n\n"
    "Size nasıl yardımcı olabilirim? 😊\n"
    "👉 Haftalık hava durumu tahminini öğrenebilir 🌤️ veya sevdiğiniz yiyeceklerin kalori miktarını kontrol edebilirsiniz 🍎.\n\n")
    id = 0
    offset = None
    previous_id = None
    while True:
        print("waiting...")
        update = Bot.getUpdates(offset)
        offset = Bot.offset_id(update)
        id = Bot.getChatid(update)
        if id != previous_id:
            Bot.chat_id = id
            Bot.sendMessage(Bot.chat_id, welcome_message)
            previous_id = id
        if offset is not None:
            print(offset)
            user_input = Bot.last_sended_text(update)
            if user_input is not None:
                splitted_user_input = user_input.split()
                splitted_user_input_lower = [word.lower() for word in splitted_user_input]
                print(splitted_user_input[0])
                helper(splitted_user_input_lower)
                weatherBot(splitted_user_input_lower)
                foodBot(splitted_user_input_lower)
            else:
                print("pass")
