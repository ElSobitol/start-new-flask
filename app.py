from flask import Flask, request
import logging
import json


app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

#Создаем запрос на корневой адрес, используем метод POST (запрос типа POST, а не GET, у нас не сайт)
@app.route('/', methods=["POST"])
def red():
    #Создаем переменную, в которую передаем request(команда, которая запоминает, какие данные пришли)
    #В нем есть json, который запоминает, какие данные туда попали, и выводит их.
    #В нашем случае, мы добавляем команду get, чтобы отследить в json запрос, в котором есть нужная нам команда
    #Как только мы что-то скажем - у нас это сразу же отобразиться!
    #Иначе ничего не произойдет
    text = request.json.get("request", {}).get("command")
    end = False
    if text == "до свидания!":
        response_text = "Пока!",
        end = True
    elif text:
        response_text = f" Вы сказали {text}"
    else:
        response_text = "Ойвэй, вы таки ничего не сказали!"
        #Далее пишем данные для классического json файла
    response = {
        "response":{
            "text": response_text,
            "end_session": end,
            "buttons":[
                {
                    "title": "wazzup, men!",
                    "hide": True

                },
                {
                    "title": "до свидания!",
                    "hide": True

                },
                {
                    "title": "Нажми на ссылку!",
                    "url": "https://www.jetbrains.com/ru-ru/pycharm/",
                    "hide": True



                }
            ]
        },
        "version": "1.0"
    }
    return json.dumps(response)
