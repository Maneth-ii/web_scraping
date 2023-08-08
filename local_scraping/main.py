from bs4 import BeautifulSoup
from lxml import *

with open("home.html", 'r') as html_file:
    content = html_file.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    courses = soup.findAll('h5')
    for course in courses:
        print(course , " \n\n ")
        with open('courses.txt', 'a')as courses_file:
            courses_file.write(str(course)+"\n")
            courses_file.close()
