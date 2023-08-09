from bs4 import BeautifulSoup
import requests

proxies = {
    'https': '118.99.127.133:8080',
    'http': '118.99.127.133:8080'
}

html = requests.get("https://www.gsmarena.com",proxies = proxies).text
soup = BeautifulSoup(html , "lxml")




all_details=[]

def get_news():
    news_elements = soup.find_all("div", class_="news-item")

    for news_element in news_elements:
        title = news_element.h3.text
        description = news_element.p.text
        posted_time = news_element.find('span', class_="meta-item-time").text
        link = news_element.a['href']
        image = news_element.img['src']
        all_details.append({
            "Title":title,
            'Description':description,
            "Posted Time" : posted_time,
            "Link":link,
            "Image":image,
        })
    return all_details

all_news = get_news()

for a_news in all_news:
    news_file = open("news.txt" , 'a')
    news_file.write(str(a_news) + '\n\n')
