from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
#driver = webdriver.Chrome('C:/Users/Seb/PycharmProjects/pythonProjectTinBo/chromedriver_win32 (1)/chromedriver.exe')
from random import seed
from random import random
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from .replacement import Check_prduct_in_order
# from secrets import username, password
# import pyautogui
global driver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument('headless')
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('???')
chrome_options.add_argument('--no-proxy-server')

# global driver

driver = webdriver.Chrome(ChromeDriverManager().install())
class Scraper:
    
    def Hit_link(self):
        driver.get('https://masada.lundimatin.biz/profil_collab/#documents_cmde_cli_recherche.php')
        driver.maximize_window()
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/div/form/div[1]/input').send_keys('lmb')
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/div/form/div[2]/input').send_keys('lmb')
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/div/form/div[2]/input').send_keys(Keys.ENTER)
        try:
            driver.find_element_by_xpath('/html/body/div/div/div/div/a[1]/div[1]/i').click()
        except:
            pass
        time.sleep(10)    
        # click on toggle butoon 
        driver.find_element_by_xpath('/html/body/div[2]/div[5]/div/div/div[1]/form/div[1]/div[1]/table/tbody/tr[3]/td[2]/div[1]/label/div').click()
    # click on advace search option
        driver.find_element_by_xpath('/html/body/div[2]/div[5]/div/div/div[1]/form/div[1]/div[4]/a').click()

        # click on = button 

    
    
        driver.find_element_by_xpath('/html/body/div[2]/div[5]/div/div/div[1]/form/div[1]/div[5]/div[2]/table/tbody/tr[2]/td[2]/div/button[1]').click()


    def Search_product(self):
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[2]/div/div/div[1]/div/form/table/tbody/tr[3]/td[2]/input').send_keys('JEFF-M65-S') 
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[2]/div/div/div[1]/div/form/table/tbody/tr[3]/td[2]/input').send_keys(Keys.ENTER)    
        time.sleep(4)
        driver.find_element_by_class_name('r_art_lib').click()  # click on hyperlink
        time.sleep(10)
        # driver.find_element_by_class_name('btn btn-secondary').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[5]/div/div/div[1]/form/div[2]/button').click() # click on Rechercher
                                        
    ###############
        time.sleep(5)
       
        res=driver.page_source
        soup=BeautifulSoup(res,'html.parser')
        div=soup.find('div',{'class':'lmb-theme'})
        oder_status=div.find_all('tr')
        # print(oder_status[0])
        order_status_list=[]
        product_name_list=[]
        for o in oder_status:
            try:
                el=o.find('span',{'class':'text-error'}) 
                if "stock insuffisant" in el.text:
     
                        product_name=o.find('a',{'target':'_blank'})
                        product_name_list.append(product_name.text.strip())

            except:
                pass
     
        Check_prduct_in_order(product_name_list, driver)