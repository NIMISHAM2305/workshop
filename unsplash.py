import requests
import os

# URL of the image
url = "https://source.unsplash.com/random/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the content of the response (image data)
    image_data = response.content

    # Define the file path for saving the image
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    image_filename = os.path.join(desktop_path, "unsplash_image.jpg")

    # Write the image data to a file
    with open(image_filename, "wb") as image_file:
        image_file.write(image_data)

    print("Image downloaded successfully at:", image_filename)
else:
    print("Failed to download image. Status code:", response.status_code)
