import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python"

# Step 1 get the pages
# Step 2 make requests
# Step 3 extract jobs


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", class_="s-pagination").find_all("a")
    print(pages)


def get_jobs():
    last_page = get_last_page()
    return []
