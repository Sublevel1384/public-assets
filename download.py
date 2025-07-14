
import requests

url = "https://beltonene-my.sharepoint.com/:x:/p/npacheco/Ef3m6BwbgLRBmORQKDB69EsBmem7EzOY9k-jg7ibS4vd5g?e=Wh4oCe&download=1"
output_file = "downloaded_file.xlsx"

response = requests.get(url)

if response.status_code == 200:
    with open(output_file, 'wb') as f:
        f.write(response.content)
    print("File downloaded successfully.")
else:
    print(f"Failed to download file. Status code: {response.status_code}")
