import requests
from bs4 import BeautifulSoup
import time

URL = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="

r = requests.get(URL)
soup = BeautifulSoup(r.content,'lxml')

jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

unfamiliar_skill = input("Enter skill that you are not familiar with: ")
print(f"Filterint out {unfamiliar_skill}")

def find_jobs():
    for index , job in enumerate(jobs):
        posted_date = job.find('span', class_='sim-posted').span.text.strip()
        if 'few' in posted_date:
            job_name = job.find('a').text.replace(' ','')
            company_name = job.find('h3', class_='joblist-comp-name').text
            skills = job.find('span',class_='srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open (f'posts/{index}.txt', 'w') as f:
                    f.write(f"Profile Name: {job_name.strip()} \n")
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More info: {more_info}")
                print(f"File saved {index}")


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting time is {time_wait} minutes...")
       # time.sleep(time_wait * 60)
