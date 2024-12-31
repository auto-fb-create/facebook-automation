import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import requests

def get_temp_email():
    # 1secmail API ব্যবহার করে নতুন টেম্পোরারি ইমেইল তৈরি
    login = "demo"  # এখানে আপনার পছন্দের লগিন ব্যবহার করতে পারেন
    domain = "1secmail.com"  # 1secmail.com ডোমেইন ব্যবহার হচ্ছে
    url = f"https://www.1secmail.com/api/v1/?action=genRandomMailbox&login={login}&domain={domain}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        email = response.json()['email']
        return email
    else:
        print("Error generating temp email")
        return None

# টেম্পোরারি ইমেইল তৈরি করা এবং প্রিন্ট করা
temp_email = get_temp_email()
print(f"Your temporary email: {temp_email}")

# Facebook সাইন-আপ URL
facebook_url = "https://www.facebook.com/r.php"

# ChromeDriver সেটআপ
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Facebook সাইন-আপ পেজে গমন
driver.get(facebook_url)

# পেজ লোড হওয়া পর্যন্ত অপেক্ষা
time.sleep(3)

# ফর্ম পূরণ করা
first_name = driver.find_element(By.NAME, "firstname")
first_name.send_keys("John")

last_name = driver.find_element(By.NAME, "lastname")
last_name.send_keys("Doe")

email_field = driver.find_element(By.NAME, "reg_email__")
email_field.send_keys(temp_email)

email_confirm = driver.find_element(By.NAME, "reg_email_confirmation__")
email_confirm.send_keys(temp_email)
def get_messages():
    # 1secmail API ব্যবহার করে টেম্পোরারি ইমেইল মেসেজ পড়া
    login = "demo"  # একই লগিন ব্যবহার করুন
    domain = "1secmail.com"  # 1secmail.com ডোমেইন ব্যবহার হচ্ছে
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        messages = response.json()
        if messages:
            for msg in messages:
                print(f"Message ID: {msg['id']}")
                print(f"From: {msg['from']}")
                print(f"Subject: {msg['subject']}")
                print(f"Date: {msg['date']}")
                print(f"Body: {msg['textBody']}\n")
        else:
            print("No messages found.")
    else:
        print("Error fetching messages")

# মেসেজগুলো প্রিন্ট করা
get_messages()
password = driver.find_element(By.NAME, "reg_passwd__")
password.send_keys("securepassword123")

# জন্ম তারিখ নির্বাচন
birth_day = driver.find_element(By.NAME, "birthday_day")
birth_day.send_keys("15")

birth_month = driver.find_element(By.NAME, "birthday_month")
birth_month.send_keys("Oct")

birth_year = driver.find_element(By.NAME, "birthday_year")
birth_year.send_keys("1995")

# লিঙ্গ নির্বাচন
gender_male = driver.find_element(By.XPATH, "//input[@value='2']")
gender_male.click()

# সাইন-আপ বোতামে ক্লিক
sign_up_button = driver.find_element(By.NAME, "websubmit")
sign_up_button.click()

# কিছু সময়ের জন্য অপেক্ষা করা
time.sleep(5)

# ব্রাউজার বন্ধ করা
driver.quit()
