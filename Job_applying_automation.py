import time, random
import undetected_chromedriver as uc
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def human_wait():
    time.sleep(random.uniform(1.5,3))

url='https://www.naukrigulf.com/python-developer-jobs?easyApply=true'
chrome_driver = 'chromedriver/chromedriver.exe'
options = uc.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-blink-features=AutomationControlled')
driver = uc.Chrome(options = options)
actions = ActionChains(driver)
driver.get(url)
sign_in = WebDriverWait(driver,15).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="ngHeader"]/div/nav/ul/li[4]/a'))
)
human_wait()
sign_in.click()
email_lab = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, 'smartEmail'))
)
email_lab.send_keys('ahmed2562006abd@gmail.com') 
human_wait()
continue_ = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="smartSubmit"]'))
)
actions.move_to_element(continue_).click().perform()
human_wait()
human_wait()
password_lab = WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.NAME, 'smartPassword'))
)
password_lab.send_keys('2562006abc')
human_wait()
login = driver.find_element(By.XPATH, '//*[@id="smartSubmit"]')
login.click()
human_wait()
human_wait()
original_window = driver.current_window_handle
jobs = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CLASS_NAME,'info-position'))
)
for i in range(len(jobs)):
    actions.move_to_element(jobs[i]).click().perform()
    human_wait()
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[-1])
    human_wait()
    try:
        easy_apply = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'.ng-btn.jd-button.blue'))
        )
        actions.move_to_element(easy_apply).click().perform()
        print(f'job {i} applyed successefully')
        human_wait()
        human_wait()
    except:
        print(f'failed to apply to job {i}')
    driver.switch_to.window(original_window)
    '''<a target="_blank" href="https://www.naukrigulf.com/python-developer-crm-sales-systems-jobs-in-dubai-uae-in-zillionaire-markets-2-to-5-years-n-cd-299645-jid-090426000100" class="info-position logo-false "><p class="designation-title">Python Developer – CRM &amp; Sales Systems</p></a>'''
    '''<button class="ng-btn jd-button blue"><img class="emblem" width="17" height="17" src="https://static.naukimg.com/s/6/205/i/white_emblem.004780c3.svg" alt="">Easy Apply</button>'''
input('hi')