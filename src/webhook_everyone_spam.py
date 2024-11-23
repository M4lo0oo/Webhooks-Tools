import threading
import requests

class EveryoneSpammer:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
        self.stop_event = threading.Event()

    def spam_everyone(self):
        while not self.stop_event.is_set():
            try:
                response = requests.post(self.webhook_url, json={"content": "@everyone Get pinged!"})
                if response.status_code == 204:
                    print("Message sent successfully.")
                else:
                    print(f"Failed to send message. Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")

    def start_spamming(self):
        self.thread = threading.Thread(target=self.spam_everyone)
        self.thread.start()

    def stop_spamming(self):
        self.stop_event.set()
        self.thread.join()

if __name__ == "__main__":
    webhook_url = input("Enter the Discord webhook URL > ")

    spammer = EveryoneSpammer(webhook_url)
    spammer.start_spamming()

    input("Press Enter to stop spamming...")
    spammer.stop_spamming()
    print("Spamming stopped.")
