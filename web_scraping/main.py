from bs4 import BeautifulSoup
import requests
import time

html_text = requests.get('https://www.cricbuzz.com/').text
soup = BeautifulSoup(html_text, 'lxml')

a = []

def get_scorecard():
    scorecard = soup.findAll('li', class_='cb-view-all-ga cb-match-card cb-bg-white')
    for a_accrd in scorecard:
        scores1_elem = a_accrd.find('div', class_='cb-hmscg-tm-bat-scr cb-font-14')
        scores2_elem = a_accrd.find('div', class_='cb-hmscg-tm-bwl-scr cb-font-14')
        
        if scores1_elem and scores2_elem:
            scores1 = scores1_elem.text
            scores2 = scores2_elem.text
            a.append({'team1': scores1, 'team2': scores2})
    return a


# file = open('mt.txt','w')

# def set_file(matches_list):
#     line = '|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|'
#     for a_match in matches_list:
#         file.write(line + "\n\n\n" + str(a_match) + "\n\n" + line +  "\n\n")


# while True:
#     matches_list = get_scorecard()
#     print(str(matches_list) + "\n\n\n")
#     # set_file(matches_list)
#     time.sleep(1)   # Pause for 11 seconds

matches_list = get_scorecard()
for match in matches_list:
    print(str(match) + "\n\n")


# file.close()