import requests
from bs4 import BeautifulSoup


def connection(url):
    """get html of website with request and parse it with soup"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    data = requests.get(url, headers=headers).content
    soup = BeautifulSoup(data, "html.parser")
    table = soup.find("table", id="economicCalendarData")
    return table


def find_time(element):
    """ find the time of each id """
    time_ = element.find("td", class_="first left time js-time").string
    return time_
