from bs4 import BeautifulSoup
import requests
import re
import os
import logging

# gov_fuel_retailers_url = "https://www.gov.uk/guidance/access-fuel-price-data"
# resp = requests.get(gov_fuel_retailers_url)
# gov_html = resp.text

# soup = BeautifulSoup(gov_html, features="html.parser")
# fuel_json_urls = soup.find_all('td')[1::2]

# website_pattern = re.compile(pattern=r"https?:\/\/([^\/]+)")
# for json_url in fuel_json_urls:
#     raw_url = json_url.get_text()
#     if "shell" not in raw_url:
#         print(f"ACCESSING RAW URL: {raw_url}")
#         current_json = requests.get(raw_url)
#         filename = re.match(pattern=website_pattern, string=raw_url)
#         filename = filename.group(1)
#         with open(f'fuel_jsons/{filename}', 'w') as file:
#             file.write(current_json.text)
#             print("file written")

# print("ok done")

website_pattern = re.compile(pattern=r"https?:\/\/([^\/]+)")
json_directory = "fuel-jsons"
def update_fuel_data() -> None:
    """Updates the directory name specified in json_directory — creating it if it doesn't exist — with the current versions of the files by scraping the goverment website they're uploaded to and downloading them."""
    
    os.makedirs(f'{json_directory}', exist_ok=True)

    gov_fuel_retailers_url = "https://www.gov.uk/guidance/access-fuel-price-data"
    resp = requests.get(gov_fuel_retailers_url)
    gov_html = resp.text

    # using BeautifulSoup to parse the page and extract the fuel retailer URLs from the table
    gov_soup = BeautifulSoup(gov_html, features="html.parser")
    fuel_json_urls = gov_soup.find_all('td')[1::2] # starts offset by 1 and steps by 2 to skip the name of the supplier, only extracting the URL

    exceptions = ["shell"]
    for json_url in fuel_json_urls:
        raw_url = json_url.get_text()
        for exception in exceptions: # shell's link is a HTML page that redirects to something that errors out for me, hence i just exclude it here
            if exception not in raw_url:
                try:
                    current_json = requests.get(raw_url)
                except Exception as e:
                    print(e)
                    continue

                filename = re.match(pattern=website_pattern, string=raw_url).group(1).replace("www.", "")
                with open(f'{json_directory}/{filename}', 'w+') as file:
                    file.write(current_json.text)

update_fuel_data()
