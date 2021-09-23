# from .hit_crm_link import Keys 
#
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

def Check_prduct_in_order(product_name_list, driver,product1,product2):
    
    # print(product_name_list)
    # li=[]
    # for p in product_name_list:
    #     li.append(p.strip())
    # print(li)    
    if str(product1) in product_name_list:
        actions = ActionChains(driver)
        
        # for _ in range(1):
        #         actions.send_keys(Keys.SPACE).perform()
        #         time.sleep(1) 
        time.sleep(20)
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[5]/div/div/div[2]/div/table[3]/tbody/tr[1]/td[8]/a[3]'))).click()

        # time.sleep(20)
        # driver.find_element_by_xpath('/html/body/div[2]/div[5]/div/div/div[2]/div/table[3]/tbody/tr[1]/td[8]/a[3]').click()
        driver.switch_to.window(driver.window_handles[1])
    #  /html/body/div[3]/div/div/div/div/div[2]/div/ul/li[4]
        time.sleep(5)
        el=driver.find_elements_by_class_name('ov_hidden')  # get all the name of product which are in order 
        # print(el,"")
        for i, e in enumerate(el):
            if  str(e.text)==str(product1):
                a='link_{}'.format(i)
                print(a,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                print(e,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                # WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[5]/div/div/div[2]/div/table[3]/tbody/tr[1]/td[8]/a[3]'))).click()
                
                driver.find_element_by_id(a).click()   #click on setting icon 
                time.sleep(10)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/div/ul/li[4]').click()
                time.sleep(10)

                driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div/div[2]/div/div/div[7]/div/div/table/tbody/tr[2]/td[4]/table/tbody/tr/td[1]/span/span').click()
                time.sleep(10)             
                driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[2]/div/div/div[1]/div/form/table/tbody/tr[3]/td[2]/input').send_keys(product2) # send prodct which we  want to replacce
                driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[2]/div/div/div[1]/div/form/table/tbody/tr[3]/td[2]/input').send_keys(Keys.ENTER) # click on add button 
                time.sleep(5)
                driver.find_element_by_class_name('lib_categorie').click()
                time.sleep(5)
                driver.find_element_by_xpath('//*[@id="form_remplacement"]/table/tbody/tr[3]/td[5]/label').click()
                driver.find_element_by_xpath('//*[@id="form_remplacement"]/table/tbody/tr[5]/td[5]/label').click()
                driver.find_element_by_xpath('//*[@id="form_remplacement"]/table/tbody/tr[6]/td[5]/label').click()
                time.sleep(7)
                driver.find_element_by_class_name('green_button').click()

                # driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/div/div[2]/div/div/div[7]/div/div/button').click()
                time.sleep(7)

                driver.find_element_by_class_name('close').click()
                
                # driver.find_element_by_xpath('').click()
                
               
                
            else:
                print(e,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

                 
            
     
        

