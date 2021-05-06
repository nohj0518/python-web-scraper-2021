import requests
from bs4 import BeautifulSoup

# soup 은 데이터 추츨하는 역할

indeed_result = requests.get("https://www.indeed.com/jobs?as_and=python&limit=50")
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", class_="pagination")

pages = pagination.find_all("a")
spans = []
for page in pages:
    spans.append(page.find("span"))
print(spans[:-1])  # 마지막 <span class = pn> item을 제외시킴
