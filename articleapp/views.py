import os
from django.shortcuts import redirect, render, HttpResponse
from django.views.generic import View
# from .hit_crm_link import Scraper
# Create your views here.
from selenium import webdriver
# from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.chrome.options import Options 
#driver = webdriver.Chrome('C:/Users/Seb/PycharmProjects/pythonProjectTinBo/chromedriver_win32 (1)/chromedriver.exe')
from random import seed
from random import random
from time import sleep, time
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
from selenium.webdriver.common.action_chains import ActionChains

def home(request):
        path_driver = '/home/sunil/workspace/sanjeevupwork/sam_code/sam_code/chromedriver'
        if request.method=="GET":
                # print(request)
                return render(request, "articleapp/home.html")
        else:
                product1=request.POST.get('Product1')
                product2=request.POST.get('Product2')

                print(product1,product2)
                option = Options()
                option.headless = True
                # driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
                driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=option)
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
                                time.sleep(30)

                                
                                WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/div/div/div[2]/div/div/div[1]/div/form/table/tbody/tr[3]/td[2]/input'))).send_keys(product1)    
                                WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/div/div/div[2]/div/div/div[1]/div/form/table/tbody/tr[3]/td[2]/input'))).send_keys(Keys.ENTER)    
                                
                                # driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[2]/div/div/div[1]/div/form/table/tbody/tr[3]/td[2]/input').send_keys(product1) 
                                driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[2]/div/div/div[1]/div/form/table/tbody/tr[3]/td[2]/input').send_keys(Keys.ENTER)    
                                time.sleep(4)
                                driver.find_element_by_class_name('r_art_lib').click()  # click on hyperlink
                                # driver.find_element_by_class_name('btn btn-secondary').click()
                                actions = ActionChains(driver)
    
                                for _ in range(3):
                                        actions.send_keys(Keys.SPACE).perform()
                                        time.sleep(1)     
                                time.sleep(30)
                      
                                WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[5]/div/div/div[1]/form/div[2]/button'))).click()
                                # b=driver.find_element_by_xpath('/html/body/div[2]/div[5]/div/div/div[1]/form/div[2]/button') # click on Rechercher
                                # driver.execute_script("arguments[0].click();", b)                              
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
                                
                                Check_prduct_in_order(product_name_list, driver,product1,product2)
                


                Scraper().Hit_link()
                Scraper().Search_product()
        return redirect('home')

class HistoryView(View):
    def get(self, request):
        return render(request, "articleapp/history.html")