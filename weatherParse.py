from bs4 import BeautifulSoup
import requests
import re
import os

linktoday = 'https://www.meteoprog.com/ru/meteograms/Krasnojarsk/' # Ссылка для погоды сегодня
link7days = 'https://krasnoyarsk.nuipogoda.ru/погода-на-неделю' # Ссылка для погоды на неделю
link30days = 'https://krasnoyarsk.nuipogoda.ru/погода-на-месяц' # Ссылка для погоды на месяц

responcetoday = requests.get(linktoday) # Подключение к ссылке для погоды один день
responce7days = requests.get(link7days) # Подключение к ссылке для погоды на 7 дней
responce30days = requests.get(link30days) # Подключение к ссылке для погоды на 30 дней

souptoday = BeautifulSoup(responcetoday.text, 'lxml') # Передача данных в суп за один день
soup7days = BeautifulSoup(responce7days.text, 'lxml') # Передача данных в суп за 7 дней
soup30days = BeautifulSoup(responce30days.text, 'lxml') # Передача данных в суп за 30 дней

def menu():
    print("Погода в Красноярске.\n1. Узнать погоду на сегодня\n2. Узнать погоду на неделю\n3. Узнать погоду на месяц\n4. Выйти")
    UserChoose = input()
    os.system('cls')
    if UserChoose == "1":
        os.system('cls')
        day()
    elif UserChoose == "2":
        os.system('cls')
        week()
    elif UserChoose == "3":
        os.system('cls')
        month()
    elif UserChoose == "4":
        exit()
    else:
        print("Такой команды не существует! Выберите команду предложенную из списка.")
        menu()

def day():

    TodayWeatherBlock = souptoday.find('table').find_all('div', class_='temperature__column') # Поиск таблицы с погодой на сегодня
    TodayWeatherList = re.findall(r"[+-]\d+", str(TodayWeatherBlock)) # Регулярное выражения для поиска градусов погоды
    TodayWeatherLen = len(TodayWeatherList) # Вычисление длины списка погоды для поиска среднего арифметического 
    TodayWeatherInt = [] # Объявление пустого списка для присваивания списку типа int
    
    for weathertoday in TodayWeatherList:
        TodayWeatherInt.append(int(weathertoday)) # Присваивание пустому списку TodayWeatherInt чисел (данных о погоде) типа int
    
    TodayWeatherSum = sum(TodayWeatherInt) # Сумма всех чисел для поиска среднего арифметического
    print(f"Погода на сегодня: {TodayWeatherSum//TodayWeatherLen}°") # Вывод среднего арифметического погоды за день

def week():

    DayWeekWeatherBlock = soup7days.find('table', class_='weather').find('tbody', class_='tbody-forecast').find_all('tr', class_='last day7') # Поиск погодного блока
    DayWeekWeatherFind = re.findall(r"<span>\d+ ...<\/span>", str(DayWeekWeatherBlock)) # При помощи регекса нахождение даты
    DayWeekWeather = re.findall(r"\d+ ...", str(DayWeekWeatherFind)) # Более точное нахождение даты
    
    WeekWeatherFindall = re.findall(r"class=.t.>.\d+", str(DayWeekWeatherBlock)) # Нахождение погоды при помощи регекса
    WeekWeatherFind = re.findall(r".\d+", str(WeekWeatherFindall)) # Более точное нахождение погоды
    
    for i in range(len(WeekWeatherFind)): # Вывод погоды на неделю
        i + 1
        print(f"{DayWeekWeather[i]} ожидается погода: {WeekWeatherFind[i]}")

def month():
    MonthWeatherBlock = soup30days.find('table', class_='weather calendar').find('tbody').find_all('td') # Нахождение блока с погодой

    MonthWeatherFindDay = re.findall(r"\d+[-][а-я]+", str(MonthWeatherBlock)) # Нахождение даты

    MonthWeatherFindallWeather = re.findall(r"class=.max.>[+-]\d+", str(MonthWeatherBlock)) # Нахождение погоды
    MonthWeatherFindWeather = re.findall(r"[+-]\d+", str(MonthWeatherFindallWeather)) # Более точное нахождение погоды

    for i in range(len(MonthWeatherFindDay)): # Вывод погоды
        i + 1
        print(f"{MonthWeatherFindDay[i]} ожидается погода: {MonthWeatherFindWeather[i]}")


if __name__ == '__main__':
    menu()