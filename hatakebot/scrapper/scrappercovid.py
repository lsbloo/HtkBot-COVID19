## Scrapper Covid


from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import os
import sys
import glob
from datetime import date
from .settings.config_variables import SETTINGS_PATHS_CONFIG_BOT,SETTINGS_PATH_SAVE_ARCH_CSV
from os import listdir



class HatakeBot(object):
    def __init__(self,path_binary_firefox,site_covid,path_save_csv):
        try:
            if path_binary_firefox == 'NOT SET FIREFOX BINARY PATH' or site_covid == 'NOT SET SITE EXAMPLE BOT' or path_save_csv == 'NOT SET PATH SAVE CSV':
                print('Error config variables Bot')
                
            else:
                self.PATH_BINARY_FIREFOX=path_binary_firefox
                self.site_covid=site_covid
                self.path_csv_save=path_save_csv 
        except Exception as e:
            print('E: Construct: ', e)


    def get_my_options(self,head_less_or_not):
        my_options = Options()
        if head_less_or_not:
            my_options.headless=False
        else:
            my_options.headless=True
        
        return my_options

    def get_my_profiles(self):
        fp = webdriver.FirefoxProfile()
        fp.set_preference("browser.download.folderList",2)
        fp.set_preference("browser.download.manager.showWhenStarting",False)
        fp.set_preference("browser.download.dir", self.path_csv_save)
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")
        fp.set_preference("pdfjs.disabled", "true")
        return fp
        
    def download_csv_page(self,head_less_or_not):
        print("Buscando Arquivo em %s ... !" %self.site_covid)
        binary = FirefoxBinary(self.PATH_BINARY_FIREFOX)
        navigator = webdriver.Firefox(firefox_profile=self.get_my_profiles(),options=self.get_my_options(head_less_or_not))
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
    
    def today_date(self,last_day,today):
        dt = date.today()
        if last_day == 1:
            q = str(dt)
            r = q.split("-")
            x = int(r[2]) - 2
            r[2] = str(x)
            f = ""
            for i in r:
                f = f + i
            return f
        elif today == 2:
            q = str(dt)
            r = q.split("-")
            x = int(r[2]) - 1
            r[2] = str(x)
            f = ""
            for i in r:
                f = f + i
            return f
        if today == 3:
            q = str(dt)
            r = q.split("-")
            f=""
            for i in r:
                f = f + i
            return f

    def last_recent_csv(self,re,last_day,today):
        candidates=[]
        validated=[]
        if last_day==1:
            for i in re:
                name = str(i).split("_")
                if len(name) > 2:
                    candidates.append({i: name})
            for k in candidates:
                for key in k.keys():
                    q = k[key][3].split(".")
                    if q[0] == self.today_date(1,0):
                        validated.append(key)
            
            return validated
        elif last_day== 2:
            for i in re:
                name = str(i).split("_")
                if len(name) > 2:
                    candidates.append({i: name})
            for k in candidates:
                for key in k.keys():
                    q = k[key][3].split(".")
                    if q[0] == self.today_date(2,0):
                        validated.append(key)
            
            return validated
        if today==3:
            for i in re:
                name = str(i).split("_")
                if len(name) > 2:
                    candidates.append({i: name})
            for k in candidates:
                for key in k.keys():
                    q = k[key][3].split(".")
                    if q[0] == self.today_date(0,3):
                        validated.append(key)
            
            return validated


    def validate_config_csv(self):
        if self.path_csv_save != None:
            re =[]
            try:
                os.chdir(self.path_csv_save)
                for file in glob.glob('*.csv*'):
                    re.append(file)
                if len(self.last_recent_csv(re,2,0)) == 0 :
                    print("ok -1")
                    if len(self.last_recent_csv(re,1,0)) == 0:
                        print('ok -2 ')
                        return self.last_recent_csv(re,0,3)[0]
                    else:
                        return self.last_recent_csv(re,1,0)[0]
                else:
                    return self.last_recent_csv(re,2,0)[0]

            except Exception as e:
                return None

        return None
    
        

def get_instance_bot():
    return HatakeBot(SETTINGS_PATHS_CONFIG_BOT[0],SETTINGS_PATHS_CONFIG_BOT[1],SETTINGS_PATH_SAVE_ARCH_CSV[0])






