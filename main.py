import requests
from bs4 import BeautifulSoup


def get_html():
    r  = requests.get(url)
    return r.text


def get_all_links():
    soup =  BeautifulSoup(html, 'html')
    links = soup.find('table', id='currencies-all').find_all('td', class='currency-name')
    


if __name__ == "__main__":
    main()