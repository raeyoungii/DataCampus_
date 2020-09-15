from crawl_naver import *
import os
import pandas as pd
from datetime import datetime


def run_single_row(keyword, category):
    crawling = Crawling(keyword, category, save_file, start_at, end_at)

    print('##################', 'keyword:', keyword, '##################')
    if crawling.open_driver():
        crawling.get_questions()
    crawling.quit_driver()
    print()


DEVELOPMENT = 'DEVELOPMENT'
PRODUCTION = 'PRODUCTION'

# option 1
current_mode = PRODUCTION

# option 2
# start_at = '20171001'
# end_at = '20171231'
start_at = None
end_at = get_today()

# define file name
save_file = ''
if start_at:
    save_file += 'from' + start_at
save_file += 'to' + end_at + '.csv'


# INITIALIZE
init_koala_nlp()
if os.path.isfile(save_file):
    os.remove(save_file)

# RUN CODE
if current_mode == DEVELOPMENT:
    run_single_row("감기", "CC")
elif current_mode == PRODUCTION:
    keywords = pd.read_csv('keyword.csv')
    print()
    for _, row in keywords.iterrows():
        run_single_row(row['keyword'], row['category'])
    print('FINISHED!')
