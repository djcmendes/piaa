import os
import requests
import zipfile
import pandas as pd
from dotenv import dotenv_values

folder_path = '../data'
tmp_folder = '../tmp'

# Load environment variables from .env file
env_vars = dotenv_values('.env')

# Define the keys for the URLs
keys = list(env_vars.keys())

# Create the data directory if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Create the data directory if it doesn't exist
if not os.path.exists(tmp_folder):
    os.makedirs(tmp_folder)

# Function to download and unzip files
def download_and_unzip(url, key, tmp_folder):

    # nome local de destino do download
    destination_path = os.path.join(tmp_folder, url.split('/')[-1])

    # Download the file
    with requests.get(url, stream=True) as r:
        r.raise_for_status()

        with open(destination_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
            print(f"Downloaded:{destination_path}", flush=True)

    # Unzip the file
    with zipfile.ZipFile(destination_path, 'r') as zip_ref:
        if not os.path.exists(tmp_folder + "/" + key):
            os.makedirs(tmp_folder + "/" + key)
            print(f"Folder created:{tmp_folder}/{key}", flush=True)
        zip_ref.extractall(tmp_folder + "/" + key)

    # Remove the zip file
    os.remove(destination_path)

# Function to download and unzip files
def convert_sas_csv_from_folder(key, tmp_folder, folder_path):
    for filename in os.listdir(tmp_folder + "/" + key):
        if filename.endswith('.sas7bdat'):
            sas_path = os.path.join(tmp_folder + "/" + key, filename)
            csv_path = os.path.join(folder_path, filename.replace('.sas7bdat', '.csv'))
            df = pd.read_sas(sas_path, format='sas7bdat')
            df.to_csv(csv_path, index=False)
            # os.remove(sas_path)
            print(f'Converted {filename} to {csv_path}')
        #else:
            # os.remove(extract_to + "/" + key + filename)

    # Remover a pasta
    if os.path.exists(folder_path + "/" + key):
        #os.rmdir(extract_to + "/" + key)
        print(f'{tmp_folder + "/" + key} foi removida.')
    else:
        print(f'{tmp_folder + "/" + key} não existe.')

# Download and unzip each file
for key in keys:
    url = env_vars.get(key)
    print(f"{key}:{url}")
    if url:
        try:
            download_and_unzip(url, key, tmp_folder)
            convert_sas_csv_from_folder(key, tmp_folder, folder_path)
            print(f"Successfully downloaded and unzipped {url}")
        except Exception as e:
            print(f"Failed to download or unzip {url}. Error: {e}")

print("All files have been processed.")