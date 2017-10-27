# Since I'm newer to Python coding, most of my code will initially
# be in the __init__.py file. I know that this is bad practice, however,
# I'm trying to focus on learning the program first. I'll go back and
# fix my improper folder structuring afterwards.

import urllib.request
import urllib.parse
import safe


try:
    # Unfortunately this API has been shut off to public use
    # Time to learn how to scrape
    token = safe.API_KEYS()
    url = 'https://community-angellist.p.mashape.com/jobs'
    headers = {}
    headers['X-Mashape-Key'] = token
    headers['Accept'] = 'application/json'

    webRequest = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(webRequest)
    respData = resp.read()

    saveFile = open('jobListings.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()
    # 401 Unauthorized

except Exception as e:
    print(str(e))
