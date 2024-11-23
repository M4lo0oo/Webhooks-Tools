import random
import time
import requests
from concurrent.futures import ThreadPoolExecutor

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'

def test_webhook(webhook_url, message="Test"):
    try:
        response = requests.post(webhook_url, json={"content": message}, timeout=5)
        if response.status_code == 204:
            return True 
        else:
            return False 
    except requests.exceptions.RequestException:
        return False 

def generate_webhook():
    print("Generating Webhooks...")

    with ThreadPoolExecutor(max_workers=10) as executor:
        while True:
            webhook_id = random.randint(100000000000000000, 999999999999999999)
            webhook_token = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=80))
            
            webhook_url = f"https://discord.com/api/webhooks/{webhook_id}/{webhook_token}"
            
            future = executor.submit(test_webhook, webhook_url)
            result = future.result()

            if result:
                print(f"{Colors.GREEN}[valid]{Colors.RESET} Webhook URL: {webhook_url}")
                return webhook_url
            else:
                print(f"{Colors.RED}[invalid]{Colors.RESET} Webhook URL: {webhook_url}")