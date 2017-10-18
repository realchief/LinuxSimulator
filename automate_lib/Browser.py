#!/usr/bin/python


from baseFunctions import *
from keyboard import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Browse():
    def __init__(self):
        self.RANDOM_BROWSE_COUNT = 0
        self.browser_x = 2
        self.browser_y = 125
        self.limit_repeat = 0
        self.opened_tabs = 1
        self.driver = None
        self.e_mail_name = ""
        self.height = 500
        self.current_page_elements = []
        self.Browser_threads = []
        self.urls = parse_csv()

    def start(self):
        time.sleep(3)
        self.driver = webdriver.Firefox(executable_path="/home/ubuntu/geckodriver")
        time.sleep(2)
        keyboard.maximize()
        time.sleep(2)

    def browsing(self, random_url, count=0):
        """
        Type url on address bar.
        :param url: 
        :return: 
        """
        if count % 2 != 0:
            keyboard.browser_open_tab()
            self.opened_tabs += 1
            time.sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[-1])
        keyboard.browser_addressbar()
        keyboard.typewrite(random_url)
        time.sleep(2)
        keyboard.hotkey('enter')
        time.sleep(4)

    def login(self):

        try:
            self.driver.get(URL['E-mail'])
            WebDriverWait(self.driver, 10)
            inbox_table = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "username")))
            time.sleep(5)

            # Type username in form field.
            username_form = self.driver.find_element_by_id('username')
            location = username_form.location
            move_click(self.browser_x + location['x'], self.browser_y + location['y'])
            time.sleep(1)
            self.e_mail_name = random.choice(list(EMAIL.keys()))
            keyboard.typemail(self.e_mail_name)
            keyboard.hotkey('TAB')

            # Type password in form field.
            password_form = self.driver.find_element_by_id('password')
            move_click(self.browser_x + password_form.location['x'], self.browser_y + password_form.location['y'])
            time.sleep(1)
            keyboard.typemail(EMAIL[self.e_mail_name])

            # Submit login button
            submit_button = self.driver.find_element_by_id('login_btn')
            location = submit_button.location
            move_click(self.browser_x + location['x'], self.browser_y + location['y'])
            time.sleep(5)

            # Wait for loading next page.
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//section[@id='pm_sidebar']")))

        except Exception as e:
            print("Browser Login function => Got Error: {}".format(e))
            self.close_borwser()

    def read_conversation_items(self):

        try:
            inbox_table = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='conversation-list-columns']")))

            print('inbox_table: {}'.format(inbox_table))
            time.sleep(3)
            inbox_lists = inbox_table.find_elements_by_class_name('conversation-meta')
            print('inbox lists: {}'.format(inbox_lists))
            print('==================================\n')
            for inbox_item in inbox_lists:
                print('inbox items: {}'.format(inbox_item))

                move_click(self.browser_x + inbox_item.location['x'], self.browser_y + inbox_item.location['y'])
                time.sleep(3)
            print('==================================\n')
        except Exception as e:
            print("Browser read_conversation_items => Got Error: {}".format(e))

    def read_inbox(self):

        try:
            inbox = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//li[@data-key='inbox']")
            inbox_location = inbox.location
            print('Inbox location: {}'.format(inbox_location))

            move_click(self.browser_x + inbox_location['x'], self.browser_y + inbox_location['y'])
            self.read_conversation_items()

        except Exception as e:
            print("Browser read_inbox got error: {}".format(e))

    def read_drafts(self):

        try:
            drafts = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//li[@data-key='drafts']")
            drafts_location = drafts.location
            print('Browser read_drafts function => drafts location: {}'.format(drafts_location))

            move_click(self.browser_x + drafts_location['x'], self.browser_y + drafts_location['y'])

            self.read_conversation_items()
        except Exception as e:
            print('Browser read_drafts function got Error: {}'.format(e))

    def read_sent(self):
        try:
            sent = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//li[@data-key='sent']")
            sent_location = sent.location
            print('Browser read_sent Function => sent location: {}'.format(sent_location))

            move_click(self.browser_x + sent_location['x'], self.browser_y + sent_location['y'])
            self.read_conversation_items()
        except Exception as e:
            print('Browser read_sent Function => Got Error: {}'.format(e))

    def read_starred(self):
        try:
            starred = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//li[@data-key='starred']")
            starred_location = starred.location
            print('Browser read_starred function => starred location: {}'.format(starred_location))

            move_click(self.browser_x + starred_location['x'], self.browser_y + starred_location['y'])
            self.read_conversation_items()
        except Exception as e:
            print('Browser read_starred function => Got Error: {}'.format(e))

    def read_archive(self):

        try:
            archive = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//li[@data-key='archive']")
            archive_location = archive.location
            print('archive location: {}'.format(archive_location))

            move_click(self.browser_x + archive_location['x'], self.browser_y + archive_location['y'])
            self.read_conversation_items()

        except Exception as e:
            print('Browser read_archive function => Got Error: {}'.format(e))

    def read_spam(self):
        try:
            spam = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//li[@data-key='spam']")
            spam_location = spam.location
            print('Browser read_spam function => spam location: {}'.format(spam_location))

            move_click(self.browser_x + spam_location['x'], self.browser_y + spam_location['y'])
            self.read_conversation_items()
        except Exception as e:
            print('Browser read_spam function => Got Error: {}'.format(e))

    def read_trash(self):

        try:
            trash = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//li[@data-key='trash']")
            trash_location = trash.location
            print('Browser read_trash function => Trash location: {}'.format(trash_location))

            move_click(self.browser_x + trash_location['x'], self.browser_y + trash_location['y'])
            self.read_conversation_items()

        except Exception as e:
            print('Browser read_trash function => Got Error: {}'.format(e))

    def compose_mail(self):
        try:
            compose = self.driver.find_element_by_xpath("//section[@id='pm_sidebar']//button")
            compose_location = compose.location
            move_click(self.browser_x + compose_location['x'], self.browser_y + compose_location['y'])

            tomail_form = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//form[@id='pm_composer']//input[@name='autocomplete']")))
            move_click(self.browser_x + tomail_form.location['x'], self.browser_y + tomail_form.location['y'])
            time.sleep(3)

            sent_mail = [item for item in EMAIL.keys() if item != self.e_mail_name]
            keyboard.typemail(sent_mail[0])
            time.sleep(3)

            keyboard.hotkey('TAB')
            title_form = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//form[@id='pm_composer']//input[@title='Subject']")))
            move_click(self.browser_x + title_form.location['x'], self.browser_y + title_form.location['y'])
            time.sleep(3)
            keyboard.typemail('From ' + self.e_mail_name)

            iframe = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//form[@id='pm_composer']//iframe[@class='squireIframe']")))
            move_click(self.browser_x + iframe.location['x'], self.browser_y + iframe.location['y'])
            time.sleep(3)
            keyboard.typemail('test')
            time.sleep(5)

            send_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//form[@id='pm_composer']//button[@data-message='message']")))
            move_click(self.browser_x + send_button.location['x'], self.browser_y + send_button.location['y'])
            time.sleep(5)

        except Exception as e:
            print('Browser compose_mail function => Got Error: {}'.format(e))

    def close_borwser(self):
        self.driver.quit()

    def logout(self):
        try:
            user_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='body']//li[@class='navigationUser']")))

            move_click(self.browser_x + user_button.location['x'], self.browser_y + user_button.location['y'])

            time.sleep(3)
            logout_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@id='body']//li[@class='navigationUser']//a[@ui-sref='login']")))

            move_click(self.browser_x + logout_button.location['x'], self.browser_y + logout_button.location['y'])

        except Exception as e:
            print('Browser logout Function => Got Error: {}'.format(e))

    def google_button(self):
        try:
            button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[@id='_fZl']")))
            move_click(self.browser_x + button.location['x'], self.browser_y + button.location['y'])

        except Exception as e:
            print('Browser Google Button => Got Error: {}'.format(e))

    def google_entry(self):
        try:
            if self.RANDOM_BROWSE_COUNT == 0:
                self.browsing('https://google.com')
                time.sleep(3)
            search_box = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.NAME, "q")))

            move_click(self.browser_x + search_box.location['x'], self.browser_y + search_box.location['y'], number=2)
            time.sleep(.5)
            move_click(self.browser_x + search_box.location['x'], self.browser_y + search_box.location['y'], number=2)
            time.sleep(3)
            keyboard.hotkey('CTRL', 'A')
            time.sleep(2)
            keyboard.typewrite(random.choice(Random_Keyword))
            self.google_button()
            self.search_google()

        except Exception as e:
            print('Browser Google Entry Function => Got Error: {}'.format(e))




browser = Browse()

if __name__ == '__main__':
    browser = Browse()
    browser.start()
    browser.popular_sites()