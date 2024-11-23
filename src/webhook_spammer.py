import requests
import threading
import time

class WebhookSpammer:
    def __init__(self, webhook_url, message, count):
        self.webhook_url = webhook_url
        self.message = message
        self.count = count
        self.stop_event = threading.Event()

    def spam(self):
        for i in range(self.count):
            if self.stop_event.is_set():
                print("Spamming stopped.")
                break
            
            response = requests.post(self.webhook_url, json={'content': self.message}, timeout=10)
            
            if response.status_code == 204:
                print(f"Message {i + 1} sent successfully.")
            else:
                print(f"Failed to send message {i + 1}. Status code: {response.status_code}")
                print(f"Response: {response.text}")
            
            time.sleep(0.1)

    def start_spamming(self):
        self.thread = threading.Thread(target=self.spam)
        self.thread.start()

    def stop_spamming(self):
        self.stop_event.set()
        self.thread.join()

if __name__ == "__main__":
    webhook_url = input("Enter the Discord webhook URL > ")
    message = input("Enter the message to spam >  ")
    count = int(input("Enter the number of times to send the message > "))

    spammer = WebhookSpammer(webhook_url, message, count)
    spammer.start_spamming()

    input("Press Enter to stop spamming...")
    spammer.stop_spamming()
