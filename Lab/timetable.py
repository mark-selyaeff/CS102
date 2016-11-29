import requests
import config
from bs4 import BeautifulSoup
import telebot
from datetime import datetime

# --------- timetable functions --------- #


def get_page(group, week=''):
    if week:
        week = str(week) + '/'
    url = '{domain}/{group}/{week}raspisanie_zanyatiy_{group}.htm'.format(
        domain=config.domain,
        week=week,
        group=group)
    response = requests.get(url)
    web_page = response.content
    return web_page

def get_schedule(web_page, day):
    soup = BeautifulSoup(web_page, "html5lib")

    # Получаем таблицу с расписанием на day

    schedule_table = soup.find("table", attrs={"id": "{}day".format(day)})

    # Время проведения занятий
    times_list = schedule_table.find_all("td", attrs={"class": "time"})
    times_list = [time.span.text for time in times_list]

    # Кабинеты
    cabs_list = schedule_table.find_all("dd", attrs={"class": "rasp_aud_mobile"})
    cabs_list = [cab.text for cab in cabs_list]

    # Место проведения занятий
    locations_list = schedule_table.find_all("td", attrs={"class": "room"})
    locations_list = [room.span.text for room in locations_list]

    # Название дисциплин и имена преподавателей
    lessons_list = schedule_table.find_all("td", attrs={"class": "lesson"})
    lessons_list = [lesson.text.split('\n\n') for lesson in lessons_list]
    lessons_list = [', '.join([info for info in lesson_info if info]) for lesson_info in lessons_list]

    return times_list, cabs_list, locations_list, lessons_list


# ------------ message handlers ------------- #

bot = telebot.TeleBot(config.access_token)

# Вывод собственных сообщений ботом
# @bot.message_handler(content_types=['text'])
# def echo(message):
#     bot.send_message(message.chat.id, message.text)

days = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 1}
timetable_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
@bot.message_handler(commands=list(days.keys()))
def get_timetable(message):
    message_lst = message.text.split()
    if len(message_lst) == 3:
        day, week, group = message_lst
    else:
        day, group = message_lst
        week = ''
    web_page = get_page(group, week)
    times_lst, cabs_lst, locations_lst, lessons_lst = get_schedule(web_page, days[day[1:]])
    resp = ''
    for time, cab, location, lesson in zip(times_lst, cabs_lst, locations_lst, lessons_lst):
        resp += '<b>{}, {}</b>, {}, {}\n'.format(time, cab, location, lesson)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')

@bot.message_handler(commands=['tommorow'])
def get_tommorow(message):
    group = message.text.split()[1]
    now = datetime.now()
    weekday = datetime.isoweekday(now) # значения (1...7)
    week_eveness = datetime.isocalendar(now)[1] % 2 + 1 # 1 - чёт, 2 - нечет
    is_week_odd = bool(datetime.isocalendar(now)[1] % 2)
    if weekday <= 6:
        web_page = get_page(group, week_eveness)
        weekday_tommorow = weekday + 1
    elif weekday == 7:
        if is_week_odd:
            web_page = get_page(group, 1)
        else:
            web_page = get_page(group, 2)
        weekday_tommorow = 1
    for value in days:
        if days[value] == weekday_tommorow:
            times_lst, cabs_lst, locations_lst, lessons_lst = get_schedule(web_page, days[value])
        break
    resp = ''
    for time, cab, location, lesson in zip(times_lst, cabs_lst, locations_lst, lessons_lst):
        resp += '<b>{}, {}</b>, {}, {}\n'.format(time, cab, location, lesson)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')

@bot.message_handler(commands=['all'])
def get_all(message):
    _, week_eveness, group = message.text.split()
    web_page = get_page(group, week_eveness)
    resp = ''
    for value in timetable_days:
        times_lst, cabs_lst, locations_lst, lessons_lst = get_schedule(web_page, days[value])
        for time, cab, location, lesson in zip(times_lst, cabs_lst, locations_lst, lessons_lst):
            resp += '<b>{}, {}</b>, {}, {}\n'.format(time, cab, location, lesson)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')




if __name__ == '__main__':
    bot.polling(none_stop=True)