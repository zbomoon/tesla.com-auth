import requests
import os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
email = os.environ['email']
password = os.environ['password']
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Accept-Encoding': 'gzip, defalate, br',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
}

if __name__ == '__main__':
    print(email, password)
    ses = requests.session()
    ses.trust_env = False
    ses.headers.update(headers)
    ses.proxies.update({'https': 'http://127.0.0.1:8888'})
    ses.verify = False
    ses.get('https://www.tesla.com/')
