from atproto import Client
from bb_configs.typ_config import TYP_LOGIN, TYP_PASSWORD, LOG_FILE
import calendar
import time
from datetime import date, datetime

BOT_FLAG = 'TYP'


def get_current_year():
    return 366 if calendar.isleap(time.gmtime()[0]) else 365


def get_day_number():
    return time.gmtime()[7]


def update_log(stroka):
    with open('thisyearprogress_log.txt', mode='a+', encoding='utf-8') as log_file:
        log_file.write(stroka)
    print(stroka)


def generate_posting_string():
    percentage_spent = round(get_day_number() / get_current_year() * 100, 2)
    # TODO minor добавить переходное значение '\u2592' // \u2588 full shade
    progress_str = ''
    count = 0
    for i in range(10):
        if count < percentage_spent:
            progress_str = progress_str + '\u2588'
            count += 10
        else:
            progress_str = progress_str + '\u2591'

    s_bsky = f'{progress_str} This year progress:, {percentage_spent}% ({get_current_year() - get_day_number()} days remaining)'

    return s_bsky


def generate_log_string(posting_flag):
    status = 'ADDED, ' if posting_flag == True else ''
    s_log = f'{datetime.now().strftime("%Y-%m-%d, %H%M%S")}, {status}{time.tzname[0]}, [{generate_posting_string()}]\n'

    return s_log


def get_latest_log_date(log_file):
    try:
        with open(log_file, mode='r', encoding='utf-8') as log_file:
            check_today = log_file.readlines()
            last_log = check_today[-1].split(',')
            log_flag = last_log[0]
        return log_flag

    except:
        return 'no log file'


def main():
    if get_latest_log_date(LOG_FILE) != str(date.today()):
        client = Client()
        client.login(TYP_LOGIN, TYP_PASSWORD)
        client.send_post(text=generate_posting_string())

        update_log(generate_log_string(True))

    else:
        update_log(generate_log_string(False))


if __name__ == '__main__':
    main()
