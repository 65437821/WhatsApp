from selenium import webdriver
import time
from bs4 import BeautifulSoup

patch="/home/demir/Masaüstü/chrome web driver/chromedriver"

browser = webdriver.Chrome(patch)
browser.get("https://web.whatsapp.com/")

time.sleep(10)
print("10 sn doldu . GO GO GO")

isim = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")
isim.send_keys("oğlum")
time.sleep(5)

sec = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]")
sec.click()
time.sleep(5)

sayac = 0
zaman  = "çevrimiçi"

soup = BeautifulSoup(browser.page_source , 'html.parser')



while(True):
    try:
        test = BeautifulSoup(browser.page_source , 'html.parser')
        s = test.find("span" , attrs = {"class":"O90ur _3FXB1"})
        zaman = s.text
    except:
        #print("1. try hatası")
        zaman =""

    while(zaman == "çevrimiçi"):
        time.sleep(1)
        sayac+=1
        try:
            al = BeautifulSoup(browser.page_source , 'html.parser')
            yeni = al.find("span" , attrs = {"class":"O90ur _3FXB1"})
            zaman = yeni.text
        except:
            #print("2. try hatası")
            zaman = ""
    if(sayac != 0):
        print(sayac,"saniye çevrimiçi oldu .")
        sayac = 0

