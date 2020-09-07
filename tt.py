# coding=utf-8
import requests

base_url = 'https://www.mochen166.net'

url_login = base_url + '/sso/login'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36"}
data = {'appId': 5,
        'cn': 'games1234',
        'password': '72f2e377f35699d835e5d7479f35531e'}
r = requests.post(url_login, data=data, headers=headers, verify=False)

url_order = base_url + '/lottery/api/u/v1/lottery/add_order'
data_order = {"lottery": "XJSSC",
              "issue": "20200907-32",
              "order": '[{"method":"dwd_dwd_dwd","code":"3||||","nums":"1","piece":"1","price":"2","odds":"19.04","point":"0","amount":"2"}]',
              "betType": 1,
              "sourceType": "0"}
r1 = requests.post(url_order, data=data_order, cookies=r.cookies, verify=False)
print(r.text)
print(r1.text)
