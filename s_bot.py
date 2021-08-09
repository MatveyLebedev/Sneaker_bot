#pyinstaller -w -F --add-binary "C:\Program Files (x86)\chromedriver.exe";"." gui_bot.py
#pyinstaller -F --noconsole gui_bot.py

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from multiprocessing import Process
import tkinter as tk
from selenium.webdriver.support.select import Select
from fake_useragent import UserAgent

headless = True
acc_per_proxy = 3

keys = ['6909-Mar-31-2021', '0587-Apr-31-2021', '0255-May-17-2021', '6994-Jun-31-2021']

acc = open('bot_accaunts.txt')
log = []
pas = []

for line in acc:
    data = line.split(' ')
    log.append(data[0])
    pas.append(data[1])

prox = open('proxy_for_bot.txt')
proxy = []
for l in prox:
    proxy.append(l)

sets = open('bot_settings.txt')

sets = list(sets)

card_number = sets[0].split(' ')[0]
month = sets[1].split(' ')[0]
year = sets[2].split(' ')[0]
cvs = sets[3].split(' ')[0]
target_URL = sets[4].split(' ')[0]
size = []
for i in range(len(sets[5].split(' ')) - 3):
    size.append(sets[5].split(' ')[i])

key = sets[6].split(' ')[0]
PATH = 'chromedriver.exe'

URL = 'https://www.adidas.ru/account-login'
URL_for_debag = 'https://www.adidas.ru/cart'

class sms_code():
    def __init__(self):
        self.code = ''
        self.flag = False

    def get(self, a):
        code = self.e.get()
        self.code = code
        self.flag = True
        self.root.destroy()

    def sms_inp(self, i):
        self.root = tk.Tk()
        frame = tk.Frame(self.root)
        self.root.configure(bg="aqua")
        self.root.title(f'sms for accaunt {i}')

        self.e = tk.Entry(width=20)
        self.b = tk.Button(text="send code", bg='black', fg='white')

        self.e.pack()
        self.b.pack()

        self.b.bind('<Button-1>', self.get)

        self.root.focus_set()
        frame.pack()
        frame.focus_set()

        self.root.mainloop()


code = sms_code()

class dri():
    def __init__(self):
        self.drivers = []
        self.inf = ''
        self.stop_flag = True


drive = dri()


option = webdriver.ChromeOptions()
option.headless = headless

d = webdriver.Chrome(executable_path=PATH, options=option, service_args=["hide_console", ])
d.get(URL)
d.close()

date = time.ctime()[8:10]
m = time.ctime().split(' ')[1]
y = time.ctime()[20:25]

def check_kry(key):
    k = key.split('-')
    if (k[1] == m) and (k[2] >= date) and (k[3] == y) and (key in keys):
        pass
    else:
        print('key error')
        # exit()

check_kry(key)

drive.inf = 'Programm starteg'

start = time.time()

def log_in(i):
    carrent_proxy = proxy[i // acc_per_proxy]
    n_option = option
    ua = UserAgent()
    userAgent = ua.random
    print(userAgent)
    n_option.add_argument(f'user-agent={userAgent}')
    n_option.add_argument(f'--poxy-server-{carrent_proxy}')   # setting proxy
    n_option.headless = headless
    drive.drivers.append(webdriver.Chrome(executable_path=PATH, options=n_option, service_args=["hide_console", ]))
    driver = drive.drivers[i]
    driver.get(URL)
    driver.maximize_window()
    wait = WebDriverWait(driver, 5)
    mail_inp = driver.find_element_by_id('login-email')
    mail_inp.send_keys(log[i])
    pasword_inp = driver.find_element_by_id('login-password')
    pasword_inp.send_keys(pas[i])
    #pasword_inp.send_keys(Keys.ENTER)
    batton = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div[1]/form/div[5]/button')
    batton.click()
    wait = WebDriverWait(driver, 5)
    time.sleep(3)
    try:
        body = driver.find_element_by_xpath('//*[@id="modal-root"]/div/div/button')
        body.click()
        print('Window closed')
    except:
        pass
    drive.inf = f'Log in {i} secsesful'

def log_in_main(i):
    carrent_proxy = proxy[i // acc_per_proxy]
    n_option = option
    ua = UserAgent()
    userAgent = ua.random
    print(userAgent)
    n_option.add_argument(f'user-agent={userAgent}')
    n_option.add_argument(f'--poxy-server-{carrent_proxy}')   # setting proxy
    n_option.headless = headless
    drive.drivers.append(webdriver.Chrome(executable_path=PATH, options=n_option, service_args=["hide_console", ]))
    driver = drive.drivers[0]
    driver.get(URL)
    wait = WebDriverWait(driver, 5)
    driver.get_screenshot_as_file("screenshot.png")
    mail_inp = driver.find_element_by_id('login-email')
    mail_inp.send_keys(log[i])
    pasword_inp = driver.find_element_by_id('login-password')
    pasword_inp.send_keys(pas[i])
    pasword_inp.send_keys(Keys.ENTER)
    #batton = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div[1]/form/div[5]/button')
    #batton.click()
    wait = WebDriverWait(driver, 5)
    time.sleep(3)
    try:
        body = driver.find_element_by_xpath('//*[@id="modal-root"]/div/div/button')
        body.click()
        print('Window closed')
    except:
        pass
    drive.inf = f'Log in {i} secsesful'

def step1(i):
    size_list = ['35.5 RU / 3.5 UK', '36 RU / 4 UK', '36.5 RU / 4.5 UK', '37 RU / 5 UK', '37.5 RU / 5.5 UK',
                 '38 RU / 6 UK',
                 '38.5 RU / 6.5 UK', '39 RU / 7 UK', '40.5 RU / 8 UK', '41 RU / 8.5 UK', '42 RU / 9 UK',
                 '42.5 RU / 9.5 UK',
                 '43 RU / 10 UK', '44 RU / 10.5 UK', '44.5 RU / 11 UK', '45 RU / 11.5 UK', '46 RU / 12 UK',
                 '46.5 RU / 12.5 UK'
                 '47 RU / 13 UK', '48 RU / 13.5 UK', '49 RU / 14 UK', '49.5 RU / 14.5 UK', '50 RU / 15 UK',
                 '51 RU / 16 UK'
                 '52 RU / 17 UK', '53 RU / 18 UK', '54 RU / 19 UK']


    while drive.stop_flag == True:
        time.sleep(1)
    driver = drive.drivers[0]
    driver.get(target_URL)
    flag = False
    while flag == False:
        try:
            size_menu = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div/div[2]/select')
            flag = True
        except:
            flag = False
            time.sleep(10)
            drive.inf = f'try {i}'
    drive.inf = f'accaunt {i} win'
    n = 0
    s = False
    while (s == False) and (n < len(size)):
        try:
            for el in size_list:
                if size[n] in el:
                    print(el)
                    size_menu = Select(driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div/div[2]/select'))
                    size_menu.select_by_visible_text(el)
                    s = True
                    break
        except:
            n += 1

    step2_batton = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div/button')
    step2_batton.click()
    drive.inf = f'size compliteg {i}'


def step2(i):
    while drive.stop_flag == True:
        time.sleep(1)
    driver = drive.drivers
    # Now we are at step2 page
    step3_batton = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/aside/div[1]/div[1]/div/div[3]/div/button')
    step3_batton.click()
    drive.inf = f'step2 complited {i}'

def step3(i):
    while drive.stop_flag == True:
        time.sleep(1)
    driver = drive.drivers[0]
    # Now we are at step3 page
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 3500)")
    time.sleep(1)
    tick_roles = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/div[11]/div/div/label/input')
    tick_roles.click()
    step4_batton = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/div[13]/button')
    step4_batton.click()
    drive.inf = f'step3 adress complited {i}'

def step4(i):
    while drive.stop_flag == True:
        time.sleep(1)
    driver = drive.drivers[0]
    # Now we are at step4 pay
    time.sleep(10)

    f = False
    while f == False:
        try:
            driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="iFrameResizer0"]'))
            f = True
        except:
            time.sleep(3)

    inp_card_number = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]/div/form/div[1]/div[1]/span/input')
    inp_card_number.send_keys(card_number)
    inp_month = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]/div/form/div[1]/div[2]/div[1]/div[2]/div/div[1]/span/input')
    inp_month.send_keys(month)
    inp_year = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]/div/form/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/span/input')
    inp_year.send_keys(year)
    inp_csv = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]/div/form/div[1]/div[2]/div[2]/div/div[1]/span/input')
    inp_csv.send_keys(cvs)
    step5_batton = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]/div/form/div[2]/button')
    step5_batton.click()

def step5(i):
    while drive.stop_flag == True:
        time.sleep(1)
    driver = drive.drivers[0]
    # Now ve are at step5
    code.sms_inp(i)
    while code.flag == False:
        time.sleep(1)

    inp_code_from_sms = driver.find_element_by_xpath('//*[@id="psw_id"]')
    inp_code_from_sms.send_keys(code.code)
    batton_finish = driver.find_element_by_xpath('//*[@id="main-content"]/form/div[3]/div/div[1]')
    batton_finish.click()
    code.flag = False
    drive.inf = f'sms conplited secsesful  {i} '

def clear_cart(i):

    time.sleep(5)
    driver = drive.drivers[i]
    driver.get('https://www.adidas.ru/cart')
    time.sleep(5)
    try:
        close_batton = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/div[2]/div/div/div/div/div/div[2]/div[1]/div[2]/div/button')
        close_batton.click()
    except:
        drive.inf = 'cart is already empty'

def activity_1(i):

    time.sleep(3)
    driver = drive.drivers[i]
    driver.get('https://www.adidas.ru/muzhchiny')
    b1 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div[2]/div/div[2]/section/nav/ul/li[4]/a')
    b1.click()
    driver.execute_script("window.scrollTo(0, 550)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 780)")
    time.sleep(10)

def step2_debag(i):
    driver = drive.drivers[0]
    driver.get(URL_for_debag)
    # Now we are at step2 page
    time.sleep(3)
    step3_batton = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/aside/div[1]/div[1]/div/div[3]/div/button')
    step3_batton.click()

def main_pipeline(i):
    drive.stop_flag = False
    log_in_main(i)
    step1(i)
    # step2_debag(i)
    step3(i)
    step4(i)
    step5(i)
    driver = drive.drivers[0]
    driver.close()
    time.sleep(3)

def generare_activity(i):
    log_in(i)
    clear_cart(i)
    activity_1(i)

def start_main():
    bot_cores = []

    for i in range(len(log)):
        while drive.stop_flag == True:
            time.sleep(1)
        bot_cores.append(Process(target=main_pipeline, args=(i,)))
        bot_cores[i].start()
        time.sleep(30)

print(time.time() - start)

