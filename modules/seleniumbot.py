""" author: feezyhendrix

    main function botcore
 """

from time import sleep
from random import randint

import modules.config as config
# importing generated info
import modules.generateaccountinformation as accnt
from modules.storeusername import store
# from .activate_account import get_activation_url
# library import
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys  # and Krates
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import imaplib
import time
import random
from fake_useragent import UserAgent
import requests
import re
import logging
import email
# from fake_useragent import UserAgent

# from pymailutils import Imap



def get_ig_code(driver, accountname):
    """
    Open the temporary mail.
    """


    action = ActionChains(driver)
   
    try:

        # Connect to the Roundcube IMAP server
        imap_server = 'gama.belldns.com'
        username = 'spam_emails@themysterypanda.info'
        password = 'iS9cZ4dkjSDmDE9'

        imap = imaplib.IMAP4_SSL(imap_server)
        imap.login(username, password)

        # Select the mailbox/folder you want to access
        mailbox = 'INBOX'
        imap.select(mailbox)

        # Search for emails addressed to a specific recipient
        status, data = imap.search(None, f'(TO "{accountname}")')

        # Get the list of email IDs
        email_ids = data[0].split()

        # Fetch the most recent email
        latest_email_id = email_ids[-1]
        status, email_data = imap.fetch(latest_email_id, '(RFC822)')

        # Process the email data
        raw_email = email_data[0][1]
        email_message = email.message_from_bytes(raw_email)
        # Print the subject
        # Extract the subject
        subject = email_message['Subject']
        subject_text = subject[:6]
        print(f"IG CODE - {subject_text}", accountname)

        # Close the connection
        imap.logout()

        for letter in subject_text:
            action.send_keys(letter).perform()
            time.sleep(0.2) 
            
        # Hit continue button
        action.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
    except:
        print(f"IG CODE - ERROR", accountname)
        driver.close()




class AccountCreator():
    account_created = 0
    def __init__(self, use_custom_proxy, use_local_ip_address):
        self.sockets = []
        self.use_custom_proxy = use_custom_proxy
        self.use_local_ip_address = use_local_ip_address
        self.url = 'https://www.instagram.com/accounts/emailsignup/'
        self.__collect_sockets()


    def __collect_sockets(self):
        r = requests.get("https://www.sslproxies.org/")
        matches = re.findall(r"<td>\d+.\d+.\d+.\d+</td><td>\d+</td>", r.text)
        revised_list = [m1.replace("<td>", "") for m1 in matches]
        for socket_str in revised_list:
            self.sockets.append(socket_str[:-5].replace("</td>", ":"))

    def createaccount(self, proxy=None):
        chrome_options = webdriver.ChromeOptions()
        if proxy != None:
            chrome_options.add_argument('--proxy-server=%s' % proxy)
            
        ua = UserAgent()
        user_agent = ua.random
        print(f"Using User-Agent: {user_agent}")

        
        ua = UserAgent()
        user_agent = ua.random
        chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"')
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")

                # chrome_options.add_argument("--incognito")
        chrome_options.add_argument('window-size=1200x600')
        #driver = webdriver.Remote(command_executor='http://45.13.59.173:4444', options=chrome_options)
        driver = uc.Chrome(chrome_options=chrome_options)

        print('Opening Browser')
        driver.get(self.url)

        print('Browser Opened')
        sleep(5)

        action_chains = ActionChains(driver)
        try:
            # Click the cookie button
            cookies_button = driver.find_element(By.XPATH, "//button[contains(.,'Alle Cookies erlauben')]")
            driver.execute_script("arguments[0].click();", cookies_button)
        except:
            print("Error accepting cookies")
            
        sleep(5)
        account_info = accnt.new_account()

        # fill the email value
        print('Filling email field')
        email_field = driver.find_element(By.NAME,'emailOrPhone')
        print(email_field)
        sleep(1)
        action_chains.move_to_element(email_field)
        print(account_info["email"])
        email_field.send_keys(str(account_info["email"]))

        sleep(2)

        # fill the fullname value
        print('Filling fullname field')
        fullname_field = driver.find_element(By.NAME,'fullName')
        action_chains.move_to_element(fullname_field)
        fullname_field.send_keys(account_info["name"])

        sleep(2)

        # fill username value
        print('Filling username field')
        username_field = driver.find_element(By.NAME,'username')
        action_chains.move_to_element(username_field)
        username_field.send_keys(account_info["username"])

        sleep(2)

        # fill password value
        print('Filling password field')
        password_field = driver.find_element(By.NAME,'password')
        action_chains.move_to_element(password_field)
        passW = account_info["password"]
        print(passW)
        password_field.send_keys(str(passW))
        sleep(1)

        sleep(2)

        try:
            submit = driver.find_element(By.XPATH,
                "//button[@type='submit']")

            driver.execute_script("arguments[0].click();", submit)

            sleep(2)
        except:
            input("PLEASE MANUALLY SUBMIT THIS FORM AND HIT ENTER")
        sleep(3)
        try:

            month_button = driver.find_element(By.XPATH, "//select")
            driver.execute_script("arguments[0].click();", month_button)

            month_button.send_keys(account_info["birthday"].split(" ")[0])
            sleep(1)

            day_button = driver.find_element(By.XPATH, "//span[2]/select")
            driver.execute_script("arguments[0].click();", day_button)

            day_button.send_keys(account_info["birthday"].split[" "][1][:-1])
            sleep(1)
            year_button = driver.find_element(By.XPATH, "//span[3]/select")
            driver.execute_script("arguments[0].click();", year_button)
            year_button.send_keys(account_info["birthday"].split[" "][2])

            sleep(2)
            submit = driver.find_element(By.XPATH,
                "//button[@type='submit']")

            driver.execute_script("arguments[0].click();", submit)

        except Exception as e :
            input("PLEASE MANUALLY SUBMIT THIS FORM AND HIT ENTER")

        get_ig_code(driver, account_info["email"])
        input("Account successfully created. Hit Enter to continue...")
        
        driver.get("https://www.instagram.com/tobiiodaasoo")
        try:
            follow_button = driver.find_element(By.XPATH, "//div[contains(.,'Folgen')]")
            driver.execute_script("arguments[0].click();", follow_button)
        except:
            input("Couldn't click Follow Button")
        # After the first fill save the account account_info
        store(account_info)
        
        """
            Currently buggy code.
        """
        # Activate the account
        # confirm_url = get_activation_url(account_info['email'])
        # logging.info("The confirm url is {}".format(confirm_url))
        # driver.get(confirm_url)

        driver.close()

    def creation_config(self):
        try:
            if self.use_local_ip_address == False:
                if self.use_custom_proxy == False:
                    for i in range(0, config.Config['amount_of_account']):
                        if len(self.sockets) > 0:
                            current_socket = self.sockets.pop(0)
                            try:
                                self.createaccount(current_socket)
                            except Exception as e:
                                print('Error!, Trying another Proxy {}'.format(current_socket))
                                self.createaccount(current_socket)

                else:
                    with open(config.Config['proxy_file_path'], 'r') as file:
                        content = file.read().splitlines()
                        for proxy in content:
                            amount_per_proxy = config.Config['amount_per_proxy']

                            if amount_per_proxy != 0:
                                print("Creating {} amount of users for this proxy".format(amount_per_proxy))
                                for i in range(0, amount_per_proxy):
                                    try:
                                        self.createaccount(proxy)

                                    except Exception as e:
                                        print("An error has occured" + e)

                            else:
                                random_number = randint(1, 20)
                                print("Creating {} amount of users for this proxy".format(random_number))
                                for i in range(0, random_number):
                                    try:
                                        self.createaccount(proxy)
                                    except Exception as e:
                                        print(e)
            else:
                for i in range(0, config.Config['amount_of_account']):
                            try:
                                self.createaccount()
                            except Exception as e:
                                print('Error!, Check its possible your ip might be banned')
                                self.createaccount()


        except Exception as e:
            print(e)


def runbot():
    account = AccountCreator(config.Config['use_custom_proxy'], config.Config['use_local_ip_address'])
    account.creation_config()
