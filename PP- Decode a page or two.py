import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
with open('file_to_save.txt', 'w') as open_file:
    for link in  soup.find_all(['p']):
        open_file.write(link.get_text()+ "\n")



#with open('file_to_save.txt', 'w') as open_file:
#    open_file.write('A string to write')