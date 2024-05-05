from atproto import Client
from bb_configs.typ_config import TYP_LOGIN, TYP_PASSWORD
from thisyearprogress import *


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
    #s_log = s_log + 'Posting flag: ' + posting_flag
    update_log(s_log)

if __name__ == '__main__':
    main()
