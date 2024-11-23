import os
from src.webhook_delete import delete
from src.webhook_spammer import WebhookSpammer
from src.webhook_info import info
from src.webhook_generator import generate_webhook
from src.webhook_editor import edit
from src.webhook_everyone_spam import EveryoneSpammer
from src.webhook_image_spammer import spam_image

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    menu = r"""
                                  
                                  
         @@@@        @@@@              
     @@@@@@@@@@@@@@@@@@@@@@@@          [owner] : M4lo0oo
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@   
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       [1] Webhook Delete
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      [2] Webhook Spammer
@@@@@@@@@@   @@@@@@@@   @@@@@@@@@@     [3] Webhook Info
@@@@@@@@@     @@@@@@     @@@@@@@@@     [4] Webhook Generator
@@@@@@@@@     @@@@@@     @@@@@@@@@     [5] Webhook Editor
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     [6] Webhook @everyone Spammer
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     [7] Webhook Image Spammer
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@    @@@@    @@@@@@@@@  
     @@@@@              @@@@@     
                                    """
    print(menu)

while True:
    clear_screen()
    display_menu()
    
    option = input("Choose an option > ")

    if option == "1":
        webhook_url = input(f"Enter Webhook URL > ")
        delete(webhook_url)
    elif option == "2":
        webhook_url = input(f"Enter Webhook URL > ")
        message = input("Enter the message to spam > ")
        count = int(input("Enter the number of times to send the message > "))

        spammer = WebhookSpammer(webhook_url, message, count)
        spammer.start_spamming()

        input("Press Enter to stop spamming...")
        spammer.stop_spamming()
    elif option == "3":
        webhook_url = input(f"Enter Webhook URL > ")
        info(webhook_url)
    elif option == "4":
        generate_webhook()
    elif option == "5":
        webhook_url = input("Enter Webhook URL > ")
        edit(webhook_url)
    elif option == "6":
        webhook_url = input("Enter the Webhook URL > ")
        spammer = EveryoneSpammer(webhook_url)
        spammer.start_spamming()

        input("Press Enter to stop the @everyone spam...")
        spammer.stop_spamming()
    elif option == "7":
        webhook_url = input("Enter Webhook URL > ")
        image_path = input("Enter the path to the image > ")
        count = int(input("Enter the number of times to send the image > "))
        spam_image(webhook_url, image_path, count)
    else:
        print("Invalid option. Please try again.")
    
    input("\nPress Enter to return to the menu...")
