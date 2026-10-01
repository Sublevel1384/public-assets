
import requests

url = "https://beltonene-my.sharepoint.com/:x:/p/helpdesk/IQDgqGXhgUVySpYcO62nC454AaWq3zPF8IHMgr1qF5cisjM?&download=1"
output_file = "downloaded_file.xlsx"

response = requests.get(url)

if response.status_code == 200:
    with open(output_file, 'wb') as f:
        f.write(response.content)
    print("File downloaded successfully.")
else:
    print(f"Failed to download file. Status code: {response.status_code}")
