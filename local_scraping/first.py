from bs4 import BeautifulSoup
from lxml import *

with open('home.html', 'r') as file:
    file_content = file.read()
    soup_file = BeautifulSoup(file_content , 'lxml')
    tags = soup_file.find_all("div", class_="card")
    for tag in tags:
        with open("card.txt" , 'a') as card_file:
            name = tag.h5.text
            description = tag.p.text
            price = tag.a.text.split()[-1]
            # price = price[len(price)-1]
            card_file.write(f'{price} - {name} - {description} \n')
            print(str(name)+"this \n\n\n")


    file.close()