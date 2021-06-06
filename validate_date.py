import requests
from requests_html import HTMLSession
from datetime import datetime

def verify_date_server():
    url = "http://localhost"
    r = requests.get(url=url)

    if not r.status_code == 200:
        raise Exception("error while getting url: {}".format(url))
    print("server is up and running")

    session = HTMLSession()
    r = session.get(url)
    r.html.render()
    date = r.html.find('h1')[0].full_text
    if not verify_date_correct(date):
        raise Exception("url date is not equal to the current date")
    print("date is valid")

def verify_date_correct(date):
    try:
        url_date = datetime.strptime(date, '%d-%m-%Y').date()
    except Exception:
        raise Exception("date not in the right format, validation failed")

    today = datetime.today().date()
    return url_date == today


if __name__ == '__main__':
    verify_date_server()

