import requests
from bs4 import BeautifulSoup
import datetime
from web.models import *
def scrap():
    url = "https://vegetablemarketprice.com/market/andhrapradesh/today"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", {"class": "table"})
        if not table:
            print("Could not find the vegetable prices table.")
            return
        rows = table.find_all("tr")
        for row in rows[1:]:
            columns = row.find_all("td")
            name = columns[1].get_text(strip=True)
            price = columns[2].get_text(strip=True)
            PastPrices.objects.create(product=name,price=int(price[1:]),date=datetime.date.today())
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the website: {e}")
if __name__ == "__main__":
    scrap()