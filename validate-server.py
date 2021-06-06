import requests


def verify_date_server():
    url = "http://localhost"
    r = requests.get(url=url)

    if not r.status_code == 200:
        print("error while getting url: {}".format(url))
        return False
    print("server is up")
    if verify_date_correct(date=None):
        return False
    return True

def verify_date_correct(date):
    return True



if __name__ == '__main__':
    verify_date_server()
