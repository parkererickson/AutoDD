from psaw import PushshiftAPI
from datetime import datetime, timedelta
import re


def get_submission(n):
    '''Returns a generator for the submission in past n days'''
    api = PushshiftAPI()
    s_date = datetime.today() - timedelta(days=n)
    s_timestamp = int(s_date.timestamp())
    gen = api.search_submissions(after=s_timestamp,
                                 subreddit='pennystocks',
                                 filter=['title', 'selftext'])
    return gen

# Get yesterday's submissions
gen = get_submission(1)
# Regex pattern
pattern = "[A-Z]{3,4}"
# Dictionary containing the summaries
title_dict = {}
selftext_dict = {}
all_dict = {}

for i in gen:
    if hasattr(i, 'title'):
        title = ' ' + i.title + ' '
        title_extracted = re.findall(pattern, title)
        for j in title_extracted:
            if j in title_dict:
                title_dict[j] += 1
            else:
                title_dict[j] = 1

            if j in all_dict:
                all_dict[j] += 1
            else:
                all_dict[j] = 1

    if hasattr(i, 'selftext'):
        selftext = ' ' + i.selftext + ' '
        selftext_extracted = re.findall(pattern, selftext)
        for j in selftext_extracted:
            if j in selftext_dict:
                selftext_dict[j] += 1
            else:
                selftext_dict[j] = 1

            if j in all_dict:
                all_dict[j] += 1
            else:
                all_dict[j] = 1
