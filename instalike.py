# Import Selenium and Webdriver to connect and interact with the Browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Import time package and sleep function in order to let the website load when it opens
from time import sleep

# Create the LikingBot Class
class LikingBot(object):

    def __init__(self, username, password, max_iter):
        
        # Past the Directory where the chromediver is in order to run it
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))        
        self.selectors = {
            "allow_all_cookies": "//div[text()='Allow all cookies']",
            "continue_with_instagram": "//div[span='Continue with Instagram']",
            "input_username": "//input[@placeholder='Username, phone or email']",
            "input_password": "//input[@placeholder='Password']",
            "button_login": "//div[text()='Log in']",
            "button_like": "//*[local-name()='svg' and @aria-label='Like']",
            "button_dismiss": "//div[span='Dismiss']"
        }

        try:
            self.login(username, password)
        except:
            print("Error while login")

        self.auto_like(max_iter)
    
    # --> Type "python3 -i main.py" in the Terminal and start developing

    def login(self, username, password):

        # 1) Go to  main website
        self.driver.get('https://www.threads.net/')

        # 1.1) Give the Website time to load; otherwise the following steps wont work
        sleep(3)

        self.driver.find_element(By.XPATH, self.selectors['continue_with_instagram']).click()
        print("conintue with instagram account")
        sleep(2)
        self.driver.find_element(By.XPATH, self.selectors['input_username']).send_keys(username)
        sleep(1)
        self.driver.find_element(By.XPATH, self.selectors['input_password']).send_keys(password)
        sleep(1)

        self.driver.find_element(By.XPATH, self.selectors['button_login']).click()
        print("login button clicked")

        sleep(10)
        try:
            self.driver.find_element(By.XPATH, self.selectors['button_dismiss']).click()
            print("dismiss button clicked!")
        except:
            print("dismiss not appear!")

        try:
            self.driver.find_element(By.XPATH, self.selectors['allow_all_cookies']).click()
            print("Allow cookies button clicked!")
        except:
            print("allow cookies not appear!")
            

        sleep(3)

    # Writing the automatic liking function
    def auto_like(self, max_iter):

        """
        Here are the elements for the automation liking. It seems like every article has the same xpath of the
        button. So the goal is to iterate through the articles with a for Loop, while the other attributes stay 
        the same!

        """

        # Start iteration
        article_iteration = 1

        while article_iteration < max_iter:
            try:
                like_buttons = WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, self.selectors['button_like'])))
                print("length",len(like_buttons))
                sleep(1)

                for like_button in like_buttons:
                    ActionChains(self.driver).move_to_element(like_button).click().perform()
                    article_iteration += 1
                    print("liked===>", article_iteration)
                    sleep(1)

                    if article_iteration >= max_iter:
                        break

            except:
                print("Error in liking the posts")

            sleep(2)
