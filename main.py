from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import json
import time
import datetime
# import os,sys

with open("setting.json", mode="r", encoding="utf-8") as jFile:
    jdata = json.load(jFile)
x = 0
i = 0
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# chromedriver_autoinstaller.install()
driver = webdriver.Chrome("./chromedriver.exe", options=options)
driver.get(
    "https://tpsr.forest.gov.tw/TPSOrder/wSite/index.do?action=indexPage&mp=1#")

while True:
    userAction = input("請輸入動作:")
    if userAction == "1":
        while True:
            localTime = time.localtime()
            TimeResult = time.strftime("%H:%M:%S", localTime)
            print(TimeResult)
            if TimeResult == jdata['runtime']:
                driver.find_element(
                    "xpath", '//*[@id="signForm"]/div[2]/input[1]').click()
                while x == 0:
                    try:
                        driver.find_element(
                            "xpath", f"/html/body/div/div[2]/div[2]/ul/li[{jdata['room']}]/form/input[1]").click()
                        x = 1
                    except:
                        pass
                # 點日期
                while x == 1:
                    try:
                        # 日期xpath
                        driver.find_element(
                            "xpath", f"//*[@id=\"calendar{jdata['calendar']}\"]/tbody/tr[{jdata['date-r']}]/td[{jdata['date-d']}]/span/a").click()
                        x = 2
                    except:
                        pass
                # 訂單明細頁面
                driver.find_element(
                    "xpath", '//*[@id="htx_iphone"]').send_keys(jdata['phone'])  # 手機號碼
                driver.find_element("xpath", '//*[@id="agree"]').click()  # 點同意
                driver.find_element(
                    "xpath", '//*[@id="form1"]/div[2]/input[1]').click()  # 點確認訂單

                while x == 2:
                    try:
                        driver.find_element(
                            "xpath", '//*[@id="htx_idnumber"]').send_keys(jdata['idnumber'])  # 身分證
                        x = 3
                    except:
                        pass
                driver.find_element(
                    "xpath", '//*[@id="htx_passport"]').send_keys(jdata['passport'])  # 護照號碼
                driver.find_element(
                    "xpath", '//*[@id="htx_name"]').send_keys(jdata['name'])  # 姓名
                driver.find_element(
                    "xpath", '//*[@id="htx_email"]').send_keys(jdata['email'])  # email
                driver.find_element(
                    "xpath", '//*[@id="htx_tel"]').send_keys(jdata['htx_tel'])  # 其他連絡電話
                ##########################
                # 日曆 未測試
                js = 'document.getElementById("htx_birthday_display").removeAttribute("readonly")'
                driver.execute_script(js)
                driver.find_element(
                    "id", 'htx_birthday_display').send_keys(Keys.CONTROL, 'a')
                driver.find_element(
                    "id", 'htx_birthday_display').send_keys(Keys.DELETE)
                driver.find_element(
                    "id", 'htx_birthday_display').send_keys(jdata['birthday'])
                ############################
                if jdata['send'] == "yes":
                    driver.find_element(
                        "xpath", '//*[@id="form1"]/div[2]/input[1]').click()
                else:
                    pass
            else:
                print("時辰未到")

    elif userAction == "2":  # 退出
        print("\n---------退出...---------")
        break
