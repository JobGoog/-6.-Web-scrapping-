# Библиотека для работы с HTTP-запросами. Будем использовать ее для обращения к API HH
import requests

# Пакет для удобной работы с данными в формате json
import json

# Модуль для работы со значением времени
import time

# Модуль для работы с операционной системой. Будем использовать для работы с файлами
import os

 
def getPage(page = 0):
        
    # Справочник для параметров GET-запроса
    params = {
        'text': 'NAME:Django,Flask', # Текст фильтра. В имени должно быть слово "Аналитик"
        'area': (1,2), # Поиск ощуществляется по вакансиям города Москва
        'page': page, # Индекс страницы поиска на HH
        'per_page': 100 # Кол-во вакансий на 1 странице
    }
    
    
    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode() 
    req.close()
    return data


# Считываем первые 2000 вакансий
for page in range(0, 1):
    
    # Преобразуем текст ответа запроса в справочник Python
    jsObj = json.loads(getPage(page))
    
    # Сохраняем файлы в папку {путь до текущего документа со скриптом}\docs\pagination
    # Определяем количество файлов в папке для сохранения документа с ответом запроса
    # Полученное значение используем для формирования имени документа
    # nextFileName = './CODES/web2/{}.json'.format(len(os.listdir('./docs/pagination')))
    
    # Создаем новый документ, записываем в него ответ запроса, после закрываем
    f = open('nextFileName.json', 'w', encoding='utf8')
    f.write(json.dumps(jsObj, ensure_ascii=False))
    f.close()
    
    # Проверка на последнюю страницу, если вакансий меньше 2000
    if (jsObj['pages'] - page) <= 1:
        break
    
    # Необязательная задержка, но чтобы не нагружать сервисы hh, оставим. 5 сек мы может подождать
    time.sleep(0.25)
    
print('Старницы поиска собраны')