import calendar
import time
from datetime import date, datetime
from atproto import Client
from bb_configs.config import TYP_LOGIN

bot_flag = 'TYP'
# keep log level in log - False - not published, True - published
posting_flag = None


def get_current_year():
    return 366 if calendar.isleap(time.gmtime()[0]) else 365


def get_day_number():
    return time.gmtime()[7]


days_rem = get_current_year() - get_day_number()
percentage_spent = round(get_day_number() / get_current_year() * 100, 2)

progress_str = ''
count = 0

# TODO minor добавить переходное значение '\u2592' // \u2588 full shade
for i in range(10):
    if count < percentage_spent:
        progress_str = progress_str + '\u2588'
        count += 10
    else:
        progress_str = progress_str + '\u2591'

# todo cute timestamp with timezones
s_bsky = f'{progress_str} This year progress:, {percentage_spent}% ({days_rem} days remaining)'
s_log = f'{datetime.now().strftime("%Y-%m-%d, %H%M%S")}, {time.tzname[0]}, {posting_flag = } {bot_flag= }, "{s_bsky}"\n'

with open('thisyearprogress_log.txt', mode='r', encoding='utf-8') as log_file:
    check_today = log_file.readlines()
    last_log = check_today[-1].split(',')
    flag = last_log[0]


# send to Bluesky
# TODO something something about password before github
def main():
    client = Client()
    client.login(TYP_LOGIN)
    client.send_post(text=s_bsky)

    print('not equal, added to bluesky', flag, str(date.today()), posting_flag)


if flag != str(date.today()):
    posting_flag = True
    if __name__ == '__main__':
        main()

else:
    posting_flag = False
    print(f'equal, {posting_flag = } ')

with open('thisyearprogress_log.txt', mode='a+', encoding='utf-8') as log_file:
    log_file.write(s_log)
