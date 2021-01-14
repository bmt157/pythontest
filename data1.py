import requests
import webbrowser
url = 'http://45.79.43.178/source_carts/wordpress/wp-admin/'
values = {'user_login': 'admin',
         'user_pass': '123456aA'}
headers = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'}
r = requests.post(url, data=values, headers=headers)
webbrowser.open(url)