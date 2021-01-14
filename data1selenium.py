from selenium import webdriver
import requests
import time


def login():
    usernamestr = 'admin'
    passwordstr = '123456aA'

    req = requests.get('http://45.79.43.178/source_carts/wordpress/wp-login.php')

    #Xu ly dang nhap va dien thong tin username, password
    driver = webdriver.Chrome("C:/Users/Admin 88/Desktop/chromedriver.exe")

    driver.get("http://45.79.43.178/source_carts/wordpress/wp-admin/")

    username = driver.find_element_by_id('user_login')
    password = driver.find_element_by_id('user_pass')
    submit = driver.find_element_by_id('wp-submit')

    username.send_keys(usernamestr)
    password.send_keys(passwordstr)
    submit.click()

    #HTML
    cookie = driver.get_cookies()[1]['value']
    print('Ten User vua Login: ')
    print(cookie.split('%')[0])

    time.sleep(1000)

if __name__ == '__main__':
    login()
