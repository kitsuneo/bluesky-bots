from atproto import Client
from bb_configs.typ_config import TYP_LOGIN, TYP_PASSWORD, LOG_FILE
import calendar
import time
from datetime import date, datetime

bot_flag = 'TYP'

def get_current_year():
    return 366 if calendar.isleap(time.gmtime()[0]) else 365


def get_day_number():
    return time.gmtime()[7]


def update_log(stroka):
    with open('thisyearprogress_log.txt', mode='a+', encoding='utf-8') as log_file:
        log_file.write(stroka)


percentage_spent = round(get_day_number() / get_current_year() * 100, 2)


def generate_posting(percentage: int):
    # TODO minor добавить переходное значение '\u2592' // \u2588 full shade
    progress_str = ''
    count = 0
    for i in range(10):
        if count < percentage_spent:
            progress_str = progress_str + '\u2588'
            count += 10
        else:
            progress_str = progress_str + '\u2591'

    return progress_str


# todo cute timestamp with timezones
s_bsky = f'{generate_posting(percentage_spent)} This year progress:, {percentage_spent}% ({get_current_year() - get_day_number()} days remaining)'
s_log = f'{datetime.now().strftime("%Y-%m-%d, %H%M%S")}, {time.tzname[0]},{bot_flag= }, "{s_bsky}"\n'


def get_latest_log_date(log_file):
    try:
        with open(log_file, mode='r', encoding='utf-8') as log_file:
            check_today = log_file.readlines()
            last_log = check_today[-1].split(',')
            log_flag = last_log[0]
        return log_flag
    except:
        print('no log file')
        return None

def main():
    if get_latest_log_date('thisyearprogress_log.txt') != str(date.today()):
        client = Client()
        client.login(TYP_LOGIN, TYP_PASSWORD)
        client.send_post(text=s_bsky)

        posting_flag = True
        print(f'not equal, {posting_flag = }')

    else:
        posting_flag = False
        print(f'equal, {posting_flag = } ')

    update_log(s_log)

if __name__ == '__main__':
    main()
