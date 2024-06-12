import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from bs4 import BeautifulSoup

username = '0357791196'
password = 'Ndln1900@#@'
link = 'https://shopee.vn/'

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
driver = uc.Chrome(options=options)
driver.get(link)
sleep(5)

try:
    #login

    driver.implicitly_wait(20)
    loginTk = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[2]/form/div[1]/div[1]/input')
    loginTk.click()
    sleep(1)
    loginTk.send_keys(username)
    sleep(1)
    driver.implicitly_wait(20)
    loginMk = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[2]/form/div[2]/div[1]/input')
    loginMk.click()
    sleep(1)
    loginMk.send_keys(password)
    sleep(1)
    driver.implicitly_wait(20)
    driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[2]/form/button').click()
    sleep(10)

    #check popup after login
    try:
        driver.implicitly_wait(8)
        popUp = driver.find_element(By.XPATH,f"//div[@aria-label='Close']")
        popUp.click()
    except:
        print('No pop up')

    # craw thiet bi dien tu
    sleep(1)
    driver.implicitly_wait(20)
    driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div/div[3]/div[2]/div[1]/div/div[2]/div/div[1]/ul/li[5]/a/div/div[2]/div').click()
    sleep(5)
    action = ActionChains(driver)
    action.send_keys(Keys.PAGE_DOWN).perform()
    sleep(1)
    action.send_keys(Keys.PAGE_DOWN).perform()
    sleep(1)
    action.send_keys(Keys.PAGE_DOWN).perform()
    sleep(1)
    action.send_keys(Keys.PAGE_DOWN).perform()
    sleep(1)
    action.send_keys(Keys.PAGE_DOWN).perform()
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.find_all(class_='col-xs-2-4 shopee-search-item-result__item')
    print(len(elements))
    for element in elements:
        childs = element.find_all(class_=['DgXDzJ rolr6k Zvjf4O','k9JZlv','OwmBnn eumuJJ','JVW3E2'])
        with open('resultCraw.txt','a',encoding='utf-8') as file:
            file.write('Tên sản phẩm: '+childs[0].text+'\n'+'Giá: '+childs[1].text+'\n'+childs[2].text+'\n'+'Vị trí: '+childs[3].text+'\n'+'------------'+'\n')
            
    sleep(10)
except Exception as e:
    print(e)
