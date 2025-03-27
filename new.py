import os
import requests
from zipfile import ZipFile

# List of brands and their logo URLs from alternative sources
brands = {
    "National_Paints": "https://brandfetch.com/national-paints",
    "Jotun": "https://brandfetch.com/jotun",
    "Terraco": "https://brandfetch.com/terraco",
    "Weber": "https://brandfetch.com/weber",
    "Polybit": "https://brandfetch.com/polybit",
    "Mapei": "https://brandfetch.com/mapei",
    "Wurth": "https://brandfetch.com/wurth",
    "Ducab": "https://brandfetch.com/ducab",
    "Schneider_Electric": "https://brandfetch.com/schneider-electric",
    "Makita": "https://brandfetch.com/makita"
}

# Directory to save logos
os.makedirs("logos", exist_ok=True)

# Function to download logo from Brandfetch
def download_logo(brand_name, url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            file_name = f"logos/{brand_name}.png"
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded {brand_name} logo.")
        else:
            print(f"Failed to download {brand_name} logo. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while downloading {brand_name} logo: {e}")

# Download logos
for brand, url in brands.items():
    download_logo(brand, url)

# Create a ZIP file
with ZipFile('brand_logos.zip', 'w') as zipf:
    for brand in brands.keys():
        file_path = f"logos/{brand}.png"
        if os.path.exists(file_path):
            zipf.write(file_path, os.path.basename(file_path))

print("Logos have been downloaded and zipped into 'brand_logos.zip'.")
