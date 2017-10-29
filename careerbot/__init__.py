# Since I'm newer to Python coding, most of my code will initially
# be in the __init__.py file. I know that this is bad practice, however,
# I'm trying to focus on learning the program first. I'll go back and
# fix my improper folder structuring afterwards.

import urllib.request
import urllib.parse
import safe
import bs4 as bs


sauce = urllib.request.openurl('https://angel.co/jobs#find/f!%7B%7D').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

print(soup.title)









# try:
'''Unfortunately this API has been shut off to public use
    Commenting out code for now. Now I must try a new method
    entirely: web scraping.
    '''

# token = safe.API_KEYS()
# url = 'https://community-angellist.p.mashape.com/jobs'
# headers = {}
# headers['X-Mashape-Key'] = token
# headers['Accept'] = 'application/json'

# webRequest = urllib.request.Request(url, headers=headers)
# resp = urllib.request.urlopen(webRequest)
# respData = resp.read()

# saveFile = open('jobListings.txt', 'w')
# saveFile.write(str(respData))
# saveFile.close()
# 401 Unauthorized

# except Exception as e:
# print(str(e))
