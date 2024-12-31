import requests
import json

# config.json থেকে কনফিগারেশন লোড করা
with open('config.json') as config_file:
    config = json.load(config_file)

def get_temp_email():
    # 1secmail API ব্যবহার করে নতুন টেম্পোরারি ইমেইল তৈরি
    login = config['temp_email_service']['login']
    domain = config['temp_email_service']['domain']
    url = f"{config['temp_email_service']['api_url']}?action=genRandomMailbox&login={login}&domain={domain}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        # JSON রেসপন্স চেক করা
        json_data = response.json()
        
        if isinstance(json_data, list) and len(json_data) > 0:
            email = json_data[0]['email']
            return email
        else:
            print("Error: No email returned in response")
            return None
    else:
        print("Error generating temp email")
        return None

# টেম্পোরারি ইমেইল তৈরি করা এবং প্রিন্ট করা
temp_email = get_temp_email()
print(f"Your temporary email: {temp_email}")
