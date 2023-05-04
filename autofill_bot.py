from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

import os
import time
options = Options()


class zyBot:
    def __init__(self):
        self.url = ""
        self.username = ""
        self.password = ""
        self.button_text = ""
        self.link_test = ""
        self.num_sections = 0
        self.driver = None

    def launch_browser(self):
        self.driver = webdriver.Chrome(options = options)
    
    def navigate_to(self, url):
        self.driver.get(url)
    
    def accept_alert(self):
        try:
            WebDriverWait(self.driver, 2).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            print("Alert accepted.")
        except TimeoutException:
            pass

    def click_button(self, xpath):
        button = self.driver.find_element(by=By.XPATH, value=xpath)
        button.click()
    
    def fill_form(self, xpath, key):
        form_fill = self.driver.find_element(by = By.XPATH, value = xpath)
        form_fill.send_keys(key)

    def wait_for_landing_page(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "section-header-row")))

            # Check for alert
            try:
                alert = self.driver.switch_to.alert
                alert.accept()
            except NoAlertPresentException:
                pass

        except TimeoutException:
            print("Landing page took too long to load.")
    # Participation Activity Filler   (short answer)
    def PA_shortAnswer_fill(self):
        # Handle alerts before waiting for the landing page
        self.accept_alert()
        # Waits until first page comes up
        self.wait_for_landing_page()

        # Finds short answer PA, and reveals all of the answers
        containers = self.driver.find_elements(By.CLASS_NAME, "content-resource.short-answer-payload.ember-view")
        for container in containers:
            buttons = container.find_elements(By.CLASS_NAME, "zb-button.secondary.show-answer-button")  
            for button in buttons:
                # Scroll the button into view
                action = ActionChains(self.driver)
                action.move_to_element(button).perform()
                button.click()
                time.sleep(0.1)
                button.click()
            # Locate all submit buttons and dialog boxes for each PA container
            submit_buttons = container.find_elements(By.CLASS_NAME, "zb-button.primary.raised.check-button") 
            dialog_boxes = container.find_elements(By.TAG_NAME, "textarea")
            answer_boxes = container.find_elements(By.CLASS_NAME, "zb-explanation.has-explanation.forfeit")


            # wait for answers to come up 
            wait = WebDriverWait(self.driver, 10)  # 10 seconds timeout
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "answers")))

            # Loop through each button and dialog box

            for submit_button, dialog_box, answer_box in zip(submit_buttons, dialog_boxes, answer_boxes):
                # Extract the text from the forfeit-answer span elements
                answer = answer_box.find_element(By.CSS_SELECTOR, ".forfeit-answer")

                # Enter the text into the dialog box
                dialog_box.send_keys(answer.text)

                # submit the answer
                submit_button.click()
                time.sleep(0.1)
        # Continue with the rest of your code
        time.sleep(0.5)

    def PA_MC_fill(self):
        # Handle alerts before waiting for the landing page
        self.accept_alert()
        # Waits until first page comes up
        self.wait_for_landing_page()
        # Finds MC PA, and reveals all of the answers
        containers = self.driver.find_elements(By.CLASS_NAME, "interactive-activity-container.multiple-choice-content-resource.participation.large.ember-view")
        for container in containers:
            questions = container.find_elements(By.CLASS_NAME, "question-choices")
            for question in questions:
                buttons = question.find_elements(By.CSS_SELECTOR, 'label[aria-hidden="true"]')
                for button in buttons:
                    # Scroll the button into view
                    action = ActionChains(self.driver)
                    action.move_to_element(button).perform()
                    button.click()
                    time.sleep(0.25)
        # Continue with the rest of your code
        time.sleep(0.5)

    def PA_animation_fill(self):
        self.accept_alert()
        self.wait_for_landing_page()
        print("made it past here1")
        containers = self.driver.find_elements(By.CLASS_NAME, "interactive-activity-container.animation-player-content-resource.participation.large.ember-view")
        for container in containers:
            print("made it past here2")
            # need start button and 2x speed button
            #2x speed button:
            fastSpeed_label = container.find_element(By.CSS_SELECTOR, 'label[aria-hidden="true"]')
            action = ActionChains(self.driver)
            action.move_to_element(fastSpeed_label).perform()
            fastSpeed_label.click()
            startButton = container.find_element(By.CLASS_NAME, "zb-button.primary.raised.start-button.start-graphic")
            startButton.click()
            time.sleep(0.1)
            #loop through play button ONLY when its not paused
            print("made it past here3")
            while True:
                try:
                    # Try to find the "Play Again" button
                    play_again_button = container.find_element(By.CSS_SELECTOR, 'button[aria-label="Play again"]')
                    break  # If the "Play Again" button is found, break the loop
                except NoSuchElementException:
                    try:
                        # Wait for the Play button to reappear
                        wait = WebDriverWait(self.driver, 0.5) 
                        play_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Play"]')))
                        action = ActionChains(self.driver)
                        action.move_to_element(play_button).perform()
                        # Click the Play button
                        play_button.click()
                        
                          # If the Play button is found and clicked, break the loop
                    except TimeoutException:
                        # If the Play button is not found within the timeout, continue waiting
                        pass
        time.sleep(0.5)

    def login(self, username, password):
        self.fill_form('/html/body/div[2]/div/div/div[1]/div[2]/input', self.username)
        self.fill_form('/html/body/div[2]/div/div/div[1]/div[3]/input', self.password)
        self.click_button('/html/body/div[2]/div/div/div[3]/button')

    def autoFill(self):
        self.launch_browser()
        section_number = "19"
        #self.url += section_number
        self.navigate_to(self.url+section_number)
        self.login(self.username, self.password)
        print("Just logged in successfully.")
        for _ in range(self.num_sections):
            #testing animation one
            self.PA_animation_fill()
            print("made it past here")
            self.PA_shortAnswer_fill()
            time.sleep(0.5)
            self.PA_MC_fill()
            time.sleep(0.5)
            section_number_int = int(section_number)
            print(section_number_int)
            section_number_int += 1
            section_number = str(section_number_int)
            next_section_url = f"{self.url}{section_number}"
            self.driver.get(next_section_url)
            self.accept_alert()  # Add this line to handle alerts before the next iteration
        self.driver.quit()
        time.sleep(5)

    def print_info(self):
        print (f'Site Information - URL: {self.url}, Username: {self.username} ')


if __name__ == "__main__":    
    user = "lforeman8404@sdsu.edu"
    pw = "Woodchuck02@"
    #url_VV = "https://www.eventlounge.co/"

    numSections = 20
    url_zyBooks = "https://learn.zybooks.com/zybook/SDSUCS514NguyenSpring2023/chapter/9/section/"
    url_zyBooks2 = "https://learn.zybooks.com/zybook/SDSUCS320GappySpring2023/chapter/10/section/"
    url_zyBooks3 = "https://learn.zybooks.com/zybook/SDSUCS320GappySpring2023/chapter/11/section/"
    url_zyBooks4 = "https://learn.zybooks.com/zybook/SDSUCS320GappySpring2023/chapter/12/section/"
    url_zyBooks5 = "https://learn.zybooks.com/zybook/SDSUCS320GappySpring2023/chapter/13/section/"
    url_zyBooks6 = "https://learn.zybooks.com/zybook/SDSUCS514NguyenSpring2023/chapter/10/section/"
    url_zyBooks7 = "https://learn.zybooks.com/zybook/SDSUCS320GappySpring2023/chapter/1/section/"

    bot = zyBot()
    '''
    bot.url = url_zyBooks2
    bot.username = user
    bot.password = pw
    bot.num_sections = numSections
    
    bot.autoFill() #this call should begin the execution of the bots work on the site.
    '''
    '''bot.url = url_zyBooks3
    bot.username = user
    bot.password = pw
    bot.num_sections = 16

    bot.autoFill() #this call should begin the execution of the bots work on the site.
    bot.url = url_zyBooks4
    bot.username = user
    bot.password = pw
    bot.num_sections = 19

    bot.autoFill() #this call should begin the execution of the bots work on the site.'''
    bot.url = url_zyBooks7
    bot.username = user
    bot.password = pw
    bot.num_sections = 6

    bot.autoFill() #this call should begin the execution of the bots work on the site.

    

