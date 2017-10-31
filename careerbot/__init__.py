# Since I'm newer to Python coding, most of my code will initially
# be in the __init__.py file. I know that this is bad practice, however,
# I'm trying to focus on learning the program first. I'll go back and
# fix my improper folder structuring afterwards.

import urllib.request
import urllib.parse
import safe
import bs4 as bs
import shelve    # Recommended by plopo/surye
import statistics as stats

url = 'https://angel.co/jobs#find/f!%7B%7D'
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req)

sauce = resp.read()
soup = bs.BeautifulSoup(sauce, 'lxml')

# IDEA: If I can't scroll and parse the page initally, I COULD try
# sorting the links, going to each job posting specifically, and
# parsing the data from the individual pages.
# The issues with this approach is making sure I get ALL the links to
# jobs I'm interested in. In this case we'd be creating a real web crawler
# Just be careful not to log duplicates, try to check for job # or title

# Approach 1) Parse all data the listings from the main job page 
# Trying to search and parse out all the job URLS I see currently
# Once this works, it needs to be able to scroll or drive down the page
for urls in soup.find_all('a'):
    every_link = urls.get('href')
    # print(every_link)

    # for jobs in every_link:
    #     print(jobs)

    # print(urls.get('href'))

# Approach 2) Get a bunch of job URLS, visit each page, and parse the 
# information from that page (easier to parse, but more work and less elegant)
# Trying to parse a single job posting page
job_url = 'https://angel.co/crunchbase/jobs/93350-quality-engineer'
req2 = urllib.request.Request(job_url, headers=headers)
resp2 = urllib.request.urlopen(req2).read()
soup2 = bs.BeautifulSoup(resp2, 'lxml')

# print(soup2.get_text())
# print('Waka waka waka')
# print(soup2.select('p'))


# Dictionary of classes used by Angellist
classes = {'Job Description': 'job-description', 'Compensation': 's-vgBottom2'}

jobDes = 'job-description'
vgBot = 's-vgBottom2'
vgTop = 's-vgBottom0_5'

print('Skills:')
for div in soup2.find_all('div', class_=vgTop):
    if div.text == 'Skills':
        info = div.find_next_sibling('div', class_=vgBot)
        print(info.string)

print('*' * 20)

print('Compensation:')
for div in soup2.find_all('div', class_=vgBot):
    if div.text == 'Compensation':
        info = div.find_next_siblings('div', class_=vgBot)
        print(info.contents)


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
