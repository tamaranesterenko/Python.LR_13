# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

import sys


date_info = {'year': input("Введите год:"),
             'month': input("Введите месяц:"),
             'day': input("Введите день:")}
track_info = {'artist': input("Введите ФИО:"),
              'title': input("Введите название произведения:")}
all_info = {**date_info, **track_info}

if __name__ == "__main__":
    print("Выведите информацию о композиторе:", all_info)





