import requests
import base64

def edit(webhook_url):
    print("=== Edit Webhook ===")
    print("1. Change Webhook Name")
    print("2. Change Webhook Avatar")
    print("3. Both Name and Avatar")
    print("4. Cancel")
    
    choice = input("Choose an option > ")
    data = {}

    if choice == "1" or choice == "3":
        new_name = input("Enter the new name for the Webhook > ")
        data["name"] = new_name

    if choice == "2" or choice == "3":
        new_avatar_path = input("Enter the file path for the new avatar image (leave blank to skip) > ")
        if new_avatar_path:
            try:
                with open(new_avatar_path, "rb") as avatar_file:
                    avatar_base64 = base64.b64encode(avatar_file.read()).decode("utf-8")
                data["avatar"] = f"data:image/png;base64,{avatar_base64}"
            except FileNotFoundError:
                print("Error: File not found. Avatar change skipped.")
    
    if not data:
        print("No changes were made.")
        return
    
    response = requests.patch(webhook_url, json=data)
    if response.status_code == 200:
        print("Webhook updated successfully!")
    else:
        print(f"Failed to update Webhook. Status code: {response.status_code}")
        print(f"Response: {response.text}")
