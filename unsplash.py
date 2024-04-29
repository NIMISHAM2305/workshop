import urllib.request
import os

# URL of the image
url = "https://source.unsplash.com/random/"

# Define the file path for saving the image
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
image_filename = os.path.join(desktop_path, "unsplash_image.jpg")

try:
    # Download the image
    urllib.request.urlretrieve(url, image_filename)
    print("Image downloaded successfully at:", image_filename)
except Exception as e:
    print("Failed to download image:", e)
