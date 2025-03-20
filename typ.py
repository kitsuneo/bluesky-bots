#!/usr/bin/python3
from atproto import Client
from bb_configs.typ_config import TYP_LOGIN, TYP_PASSWORD, LOG_FILE
import calendar
import time
from datetime import date, datetime


# TODO create pretty config, check if config doesnt exist create the one with default settings
# TODO Major add run by cron
# TODO pyproject.toml

def get_current_year():
    return 366 if calendar.isleap(time.gmtime()[0]) else 365


def get_day_number():
    return time.gmtime()[7]


def generate_posting_string():
    days_spent = round(get_day_number() / get_current_year() * 100)
    print(days_spent)
    days_rem = get_current_year() - get_day_number()

    progress_str = ''
    count = 0
    for i in range(10):
        if count < days_spent:
            progress_str = progress_str + '\U0001F7E6'
            count += 10
        else:
            progress_str = progress_str + '\U00002B1C'

    s_bsky = f'[{progress_str}]\nThis year progress: {days_spent}% ({days_rem} days remaining)'

    return s_bsky


def generate_log_string(posting_flag):
    status = 'ADDED' if posting_flag else 'not added'
    #TODO Minor make cute timezone part of the date string
    s_log = f'{datetime.now().strftime("%Y-%m-%d, %H%M%S, %z")}, {status}, {time.tzname[0]}, {generate_posting_string()}\n'

    return s_log


def get_latest_log_date(log_file):
    try:
        with open(log_file, mode='r', encoding='utf-8') as log_file:
            check_today = log_file.readlines()
            last_log = check_today[-1].split(',')
        return last_log[0]

    except:
        return 'no log file'


def update_log(stroka):
    with open(LOG_FILE, mode='a+', encoding='utf-8') as log_file:
        log_file.write(stroka)
    print(stroka)


def main():
    """
    If latest record in log file == today, meaning the bot already posted the message, no need for other postings
    """

    if get_latest_log_date(LOG_FILE) == str(date.today()):
        update_log(generate_log_string(False))

    else:
        client = Client()
        client.login(TYP_LOGIN, TYP_PASSWORD)
        client.send_post(text=generate_posting_string())

        update_log(generate_log_string(True))


if __name__ == '__main__':
    main()
