import requests

def delete(webhook_url):
    try:
        response = requests.delete(webhook_url, timeout=10)

        if response.status_code == 204:
            print("Webhook successfully deleted.")
        else:
            print(f"Error : {response.status_code}")

    except requests.exceptions.Timeout:
        print("Timed out. Try again later.")
    except requests.exceptions.RequestException as e:
        print(f"Error : {e}")