from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from time import sleep
import pickle
import webbrowser
import pygetwindow as gw

link = 'https://shopee.vn/'

username = '0357791196'
password = 'Ndln1900@#@'

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"


try:
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open(link)
    browser_window_title = None
    for window in gw.getAllTitles():
        if " - Google Chrome" in window:  # Thay 'Google Chrome' bằng tên của trình duyệt bạn sử dụng
            browser_window_title = window
            break

    sleep(5)
    if browser_window_title:
        # Khởi tạo WebDriver Chrome và chuyển đổi sang cửa sổ đã mở
        # options = Options()
        # options.add_argument("user-data-dir=selenium")  # Lưu trạng thái đăng nhập
        browser = webdriver.Chrome()
        browser.get('about:blank')  # Mở trang trống trước để tránh lỗi
        browser.execute_script(f"window.open('{link}', '{browser_window_title}');")  # Mở trang web trong cửa sổ đã mở
        browser.switch_to.window(browser_window_title)
        # browser.get(link)
        print('26')
        browser.implicitly_wait(20)
        loginTk = browser.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[2]/form/div[1]/div[1]/input')
        loginTk.click()
        sleep(2)
        print('31')
        loginTk.send_keys(username)
        sleep(2)
        browser.implicitly_wait(20)
        loginMk = browser.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[2]/form/div[2]/div[1]/input')
        loginMk.click()
        loginMk.send_keys(password)
        sleep(5)
        browser.implicitly_wait(20)
        browser.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[2]/form/button').click()
    
        sleep(50)
except Exception as e:
    print(e)


