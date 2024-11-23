import requests

def spam_image(webhook_url, image_path, count):
    """
    Fonction pour envoyer une image via un Webhook plusieurs fois.

    :param webhook_url: L'URL du Webhook Discord
    :param image_path: Le chemin local de l'image
    :param count: Le nombre de fois à envoyer l'image
    """
    try:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()

        files = {
            "file": ("image.png", image_data, "image/png")
        }

        for _ in range(count):
            response = requests.post(webhook_url, files=files)

            if response.status_code == 204:
                print("Image sent successfully.")
            else:
                print(f"Failed to send image. Status code: {response.status_code} - {response.text}")

    except FileNotFoundError:
        print(f"Error: The image file at {image_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")