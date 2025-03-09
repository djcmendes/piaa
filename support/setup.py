import os
import requests
import zipfile
from dotenv import dotenv_values

extract_to = '../data'

# Load environment variables from .env file
env_vars = dotenv_values('.env')

# Define the keys for the URLs
keys = list(env_vars.keys())

# Create the data directory if it doesn't exist
if not os.path.exists(extract_to):
    os.makedirs(extract_to)

# Function to download and unzip files
def download_and_unzip(url, folder_path=extract_to):
    local_filename = url.split('/')[-1]

    # Download the file
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    # Unzip the file
    with zipfile.ZipFile(local_filename, 'r') as zip_ref:
        zip_ref.extractall(folder_path)

    # Remove the zip file
    os.remove(local_filename)

# Download and unzip each file
for key in keys:
    url = env_vars.get(key)
    print(f"{key}:{url}")
    if url:
        try:
            download_and_unzip(url)
            print(f"Successfully downloaded and unzipped {url}")
        except Exception as e:
            print(f"Failed to download or unzip {url}. Error: {e}")

print("All files have been processed.")