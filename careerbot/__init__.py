# Since I'm newer to Python coding, most of my code will initially
# be in the __init__.py file. I know that this is bad practice, however,
# I'm trying to focus on learning the program first. I'll go back and
# fix my improper folder structuring afterwards.

import urllib.request
import urllib.parse
import safe


try:
    token = safe.API_KEYS()
    url = 'https://community-angellist.p.mashape.com/jobs'
    print(token)
    # EUREKA!

except Exception as e:
    print(str(e))
