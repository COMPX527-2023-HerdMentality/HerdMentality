import pandas as pd
import requests
from urllib.parse import urlparse
import os
import argparse

# Create the 'images' directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Define a custom user agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
}

# Function to download and save images
def download_images(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Iterate through the rows and download images
    for index, row in df.iterrows():
        name = row[0]
        image_url = row['image']

        # Parse the image URL to get the file extension
        parsed_url = urlparse(image_url)
        file_extension = os.path.splitext(parsed_url.path)[1]

        # Replace spaces with underscores in the name
        name = name.replace(" ", "_")

        # Generate the filename
        filename = f"images/{name}{file_extension}"  # Save in the 'images' directory

        try:
            # Download the image with the custom user agent
            response = requests.get(image_url, headers=headers)

            if response.status_code == 200:
                with open(filename, 'wb') as file:
                    file.write(response.content)
                    print(f"Downloaded {filename}")
            elif response.status_code == 403:
                print(f"Failed to download {filename} - Access Denied (HTTP 403)")
            else:
                print(f"Failed to download {filename} - Status Code: {response.status_code}")
        except Exception as e:
            print(f"Failed to download {filename} - Exception: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download images from a CSV file")
    parser.add_argument("csv_file", help="Path to the CSV file containing actor names and image URLs")
    args = parser.parse_args()

    download_images(args.csv_file)
