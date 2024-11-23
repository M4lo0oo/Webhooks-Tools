import requests

def info(webhook_url):
    try:
        webhook_id, webhook_token = webhook_url.split('/')[-2:]
    except ValueError:
        print(f"Invalid webhook URL format.")
        return

    try:
        response = requests.get(f'https://discord.com/api/webhooks/{webhook_id}/{webhook_token}')
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return

    webhook_info = response.json()

    print(f"Webhook Information")
    print(f"==================")
    print(f"ID: {webhook_info.get('id', 'N/A')}")
    print(f"Name: {webhook_info.get('name', 'N/A')}")
    print(f"Channel ID: {webhook_info.get('channel_id', 'N/A')}")
    print(f"Guild ID: {webhook_info.get('guild_id', 'N/A')}")
    print(f"Avatar: {webhook_info.get('avatar', 'N/A')}")
    print(f"Token: {webhook_token}")
    print(f"Type: {webhook_info.get('type', 'N/A')}")
    print(f"Application ID: {webhook_info.get('application_id', 'N/A')}")
    print(f"Source Guild: {webhook_info.get('source_guild', 'N/A')}")
    print(f"Source Channel: {webhook_info.get('source_channel', 'N/A')}")
    print(f"URL: {webhook_url}")