import requests
import json

def get_temp_email():
    config = json.load(open('config.json'))
    login = config["temp_email"]
    domain = config["domain"]
    
    url = f"https://www.1secmail.com/api/v1/?action=genRandomMailbox&login={login}&domain={domain}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = response.json()
        
        if isinstance(json_data, list) and len(json_data) > 0:
            return json_data[0]
        else:
            print("Error: No email returned in response")
            return None
    else:
        print("Error generating temp email")
        return None

def create_facebook_account():
    config = json.load(open('config.json'))
    temp_email = get_temp_email()
    
    if temp_email:
        facebook_url = config["facebook_signup_url"]
        data = {
            "first_name": config["facebook_data"]["first_name"],
            "last_name": config["facebook_data"]["last_name"],
            "email": temp_email,
            "password": config["facebook_data"]["password"],
            "dob": config["facebook_data"]["dob"],
            "gender": config["facebook_data"]["gender"]
        }
        
        response = requests.post(facebook_url, data=data)
        
        if response.status_code == 200:
            print("Account successfully created!")
        else:
            print("Failed to create account.")
    else:
        print("Failed to get a temporary email.")

if __name__ == "__main__":
    create_facebook_account()
