from bs4 import BeautifulSoup

with open('home.html','r') as html_files:
    content = html_files.read()

    soup = BeautifulSoup(content,'lxml')
    #print(soup.prettify())

    card_courses = soup.find_all('div', class_='card')

    for course in card_courses:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f"{course_name} for {course_price}")