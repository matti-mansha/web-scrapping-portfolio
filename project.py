from bs4 import BeautifulSoup
import requests


def request(url):
    return requests.get(url)


def crypto_info_printer(top_information, coin_name, coin_price, market_cap):
    info = ""
    for i in range(5):
        x = top_information[i].text
        info = info + x + "\n****************************\n"

    info = info + "NAME\t\tPrice\t\t\tMarket Cap\n"

    for i in range(9, 19):
        x = coin_name[i].text
        info = info + x + "     "
        y = coin_price[i - 6].text
        info = info + y + "     "
        z = market_cap[i-9].text
        info = info + z + "     "
        info = info + "\n-----------------------------\n"
    print(info)


def soup_lxml(text):
    return BeautifulSoup(text, 'lxml')


def crypto_info(url):
    response = request(url)     # request url, in this case 'https://coinmarketcap.com/'
    html_text = response.text   # html text of that request

    soup = soup_lxml(html_text)      # convert html text to lxml format

    # Required Data from website
    top_information = soup.find_all('span', class_='sc-2bz68i-0 cVPJov')
    coin_name = soup.find_all(class_='sc-1eb5slv-0 iworPT')
    coin_price = soup.find_all(class_='sc-131di3y-0')
    market_cap = soup.find_all(class_='sc-1ow4cwt-1 ieFnWP')

    crypto_info_printer(top_information, coin_name, coin_price, market_cap)


if __name__ == '__main__':
    url = 'https://coinmarketcap.com/'
    crypto_info(url)
