from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import random
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(r'C:\Users\SABAREESH\Desktop\intern\chromedriver.exe')#add your webdriver location

driver.maximize_window() #Maximize the chrome window
sleep(1)

def login(u_name,p_word):
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    username.send_keys(u_name)
    password.send_keys(p_word)
    sleep(2)
    
    Login_Button = WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']")))
    Login_Button.click()

        # Not now Save info for Login

    Not_now=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(text(),"Not Now")]'))).click()

        # Not now for notifications
    Not_now2=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(text(),"Not Now")]'))).click()

    sleep(3)



def Hashtags(hashtag_list=[],num=5):
    user_list = []
    new_followed = []
    followed = 0
    for hashtag in hashtag_list:
        driver.get('https://www.instagram.com/explore/tags/'+ hashtag + '/')
        sleep(5)
        driver.execute_script("window.scrollTo(0,4000);")
        first_thumb = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
        first_thumb.click()

        sleep(3)
        try:
            for members in range(1,num):

                username = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[1]/span/a').text
                if username not in user_list:

                    if driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[2]/button').text == 'Follow' :
                        
                        #follow
                        driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[2]/button').click()
                        new_followed.append(username)
                        followed += 1

                        #like
                        driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[2]/section[1]/span[1]/button').click()
                        sleep(2)

                        #comment
                        comm_prob = random.randint(1,10)

                        if comm_prob > 7:
                            driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[2]/section[1]/span[2]/button').click()
                            try:
                                driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/button[2]').click()
                                sleep(2)
                            except:
                                pass
                            try:
                                comment_box = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')


                                if (comm_prob > 7) and (comm_prob < 9):
                                    comment_box.send_keys('Nice work :)')
                                    sleep(1)
                                elif comm_prob == 9:
                                    comment_box.send_keys('Nice gallery!!')
                                    sleep(1)
                                elif comm_prob == 10:
                                    comment_box.send_keys('So cool! :)')
                                    sleep(1)

                                comment_box.send_keys(Keys.ENTER)
                                sleep(2)
                            except:
                                continue
                            try:
                                driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/button[2]').click()
                                sleep(2)
                            except:
                                continue
                    driver.find_element_by_link_text('Next').click()
                    sleep(1)
                else:
                    user_list.append(username)
                    driver.find_element_by_link_text('Next').click()
                    sleep(1)
        except:
            continue

    return new_followed


ac=ActionChains(driver)


def Feed(num):
    for i in range(1,num):
        
    # Feed liking
        try:
            post=driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div/div[3]/div/article['+str(i)+']/div/div[2]/div/div[1]/div[2]')
            ac.double_click(post).perform()
            sleep(2)
        except:
            continue
        
        

    # Feed commenting
        try:
            driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div/div[3]/div/article[1]/div/div[3]/div/div/section[3]/div/form/textarea').click()
            sleep(1)
            coment_box=driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div/div[3]/div/article['+str(i)+']/div/div[3]/div/div/section[3]/div/form/textarea')
            com_prob=random.choice(['Nice work!', 'WOW!!','Excellent!!!','Superb :)','Awesome!'])
            coment_box.send_keys(com_prob)
            coment_box.send_keys(Keys.ENTER)
            sleep(3)
        except:
            continue
        try:
            driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/button[2]').click()
            sleep(2)
        except:
            continue

        



#Driver Code

# if __name__=='__main__':

u_name='intern831'
p_word='account456'

# Trial Account
# u_name='uda.tej.sab'
# p_word='account123'

hashtag_list = ['nature', 'naturephotography', 'traveler']
login(u_name,p_word)
Feed(5)
print(Hashtags(hashtag_list),5)
driver.close()