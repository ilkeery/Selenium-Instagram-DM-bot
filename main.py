from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


email ='YOUR IG MAIL'
password ='YOUR IG PASSWORD'

class Instagram:
    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.browser = webdriver.Chrome()
        # If you get path error use this.
        #self.browser = webdriver.Chrome(executable_path='YOUR CHROME DRIVER PATH')
        
    def signIn(self):
        try:
            self.browser.get("https://www.instagram.com/")
            time.sleep(3)
            self.browser.maximize_window()
            time.sleep(1.5)
            self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.email)
            time.sleep(2.5)
            self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.password)
            time.sleep(2.5)
            self.browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div").click()
            time.sleep(5)
            
        except Exception as err:
            print(f"Sign-in error --->{err}")
            raise
    
    def sendMessage(self,username,message):
        try:
            self.username = username
            self.message = message
            self.browser.get("https://www.instagram.com/direct/inbox/")
            time.sleep(5)
            print("XXXXXXXX")

            self.browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
            time.sleep(5)
            self.browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div/div[3]/div/button").click()
            time.sleep(5)
            self.browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input").send_keys(username)
            time.sleep(5)
            users = self.browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]")
            userId=users.find_elements(By.CSS_SELECTOR,"div[class='x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj']")
            
            for user in userId:
                print(user.text)
                if(user.text==username):
                    break 
            time.sleep(1)
            user.click()
            time.sleep(3)
            self.browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button").click()
            time.sleep(3)
            textField = self.browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(message)
            time.sleep(2)
            textField.send_keys(Keys.ENTER)
            time.sleep(2)
        except Exception as err:
            print(f"Sending message error. -->{err}")
            raise

    def close(self):
        self.browser.close()
        print("Accomplished Successfully.")



instagramBot = Instagram(email=email,password=password)
instagramBot.signIn()
instagramBot.sendMessage("Receiver's ig id(Example:alexa123)","Write your message here..")
instagramBot.close()