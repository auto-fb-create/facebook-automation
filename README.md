import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import requests

# র‍্যান্ডম নাম তৈরি করার ফাংশন
def generate_random_name():
    first_names = ["John", "Jane", "Alex", "Sara", "Mike", "Emily"]
    last_names = ["Smith", "Brown", "Taylor", "Anderson", "Lee"]
    return random.choice(first_names) + " " + random.choice(last_names)

# র‍্যান্ডম ইমেইল তৈরি করার ফাংশন
def generate_temp_email():
    response = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox")
    if response.status_code == 200:
        return response.json()[0]
    return None

# ব্রাউজার সেটআপ (headless mode)
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

# Facebook সাইনআপ ফর্ম খুলুন
driver.get("https://www.facebook.com/")
time.sleep(3)

try:
    # র‍্যান্ডম তথ্য তৈরি করুন
    full_name = generate_random_name()
    email = generate_temp_email()
    password = "Password123!"
    day = str(random.randint(1, 28))
    month = str(random.randint(1, 12))
    year = str(random.randint(1980, 2005))

    # সাইনআপ ফর্ম পূরণ করুন
    first_name_input = driver.find_element(By.NAME, "firstname")
    last_name_input = driver.find_element(By.NAME, "lastname")
    email_input = driver.find_element(By.NAME, "reg_email__")
    password_input = driver.find_element(By.NAME, "reg_passwd__")
    day_input = driver.find_element(By.ID, "day")
    month_input = driver.find_element(By.ID, "month")
    year_input = driver.find_element(By.ID, "year")
    gender_input = driver.find_element(By.XPATH, "//input[@value='2']")  # Male: '2'

    first_name_input.send_keys(full_name.split(" ")[0])
    last_name_input.send_keys(full_name.split(" ")[1])
    email_input.send_keys(email)
    password_input.send_keys(password)
    day_input.send_keys(day)
    month_input.send_keys(month)
    year_input.send_keys(year)
    gender_input.click()

    # সাইনআপ বাটনে ক্লিক করুন
    submit_button = driver.find_element(By.NAME, "websubmit")
    submit_button.click()

    print(f"অ্যাকাউন্ট তৈরি হচ্ছে: {full_name}, ইমেইল: {email}")

    # অপেক্ষা করুন
    time.sleep(10)

except Exception as e:
    print(f"ত্রুটি হয়েছে: {e}")

# ব্রাউজার বন্ধ করুন
driver.quit()
