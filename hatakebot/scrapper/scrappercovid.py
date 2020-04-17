## Scrapper Covid


from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
import time
import os
import sys
import glob
from datetime import date



class HatakeBot(object):
    def __init__(self,path_binary_firefox,site_covid,path_save_csv):
        try:
            if path_binary_firefox == None or site_covid == None or path_save_csv == None:
                print('Error config variables Bot')
            else:
                self.PATH_BINARY_FIREFOX=path_binary_firefox
                self.site_covid=site_covid
                self.path_csv_save=path_save_csv
        except Exception as e:
            print('E: Construct: ', e)


    def get_my_profiles(self):
        fp = webdriver.FirefoxProfile()
        fp.set_preference("browser.download.folderList",2)
        fp.set_preference("browser.download.manager.showWhenStarting",False)
        fp.set_preference("browser.download.dir", self.path_csv_save)
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")
        fp.set_preference("pdfjs.disabled", "true")
        return fp
        
    def download_csv_page(self):
        print("Carregando Driver... !")
        binary = FirefoxBinary(self.PATH_BINARY_FIREFOX)
        navigator = webdriver.Firefox(firefox_profile=self.get_my_profiles())
        navigator.set_page_load_timeout(20)
        navigator.get(self.site_covid)
        html = navigator.page_source
        root = navigator.find_elements_by_tag_name('ion-button')
        for i in range(101):
            time.sleep(0.1)
            print(i,"%", end=" ")
    
        res = root[3].click()
        
        print()
        print()
        print("Arquivo Covid19.csv Baixado!")
        return html
    def soup(self,html):
        print()
        parset = BeautifulSoup(html,'html.parser')
        return parset
    
    def today_date(self):
        dt = date.today()
        q = str(dt)
        r = q.split("-")
        x = int(r[2]) - 1
        r[2] = str(x)
        f = ""
        for i in r:
            f = f + i
        return f
        
    def last_recent_csv(self,re):
        candidates=[]
        validated=[]
        for i in re:
            name = str(i).split("_")
            if len(name) > 2:
                candidates.append({i: name})
        for k in candidates:
            for key in k.keys():
                q = k[key][3].split(".")
                if q[0] == self.today_date():
                    validated.append(key)
        
        return validated

    def validate_config_csv(self):
        if self.path_csv_save != None:
            re =[]
            for file in glob.glob('*.csv*'):
                re.append(file)
            
            return self.last_recent_csv(re)[0]
        return None
    
        
        
PATH_BINARY_FIREFOX= '/usr/bin/firefox'
SITE_EXAMPLE='https://covid.saude.gov.br/'
PATH_SAVE="/home/osvaldoairon/"

bot = HatakeBot(PATH_BINARY_FIREFOX,SITE_EXAMPLE,PATH_SAVE)
#html_load = bot.download_csv_page()
#bot.soup(html_load)
bot.validate_config_csv()

