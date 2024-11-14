from bs4 import BeautifulSoup
import requests

gov_fuel_retailers_url = "https://www.gov.uk/guidance/access-fuel-price-data"
resp = requests.get(gov_fuel_retailers_url)
gov_html = resp.text

soup = BeautifulSoup(gov_html, features="html.parser")
# print(soup.prettify())
fuel_json_urls = soup.find_all('td')[1::2]
for json_url in fuel_json_urls:
    print(json_url.get_text())