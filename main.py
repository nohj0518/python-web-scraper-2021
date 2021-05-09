import requests
from bs4 import BeautifulSoup

# soup 은 데이터 추츨하는 역할

indeed_result = requests.get("https://indeed.com/jobs?q=python&limit=50&start=99999")
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", class_="pagination")

links = pagination.find_all("a")
pages = []
for link in links[:-1]:
    pages.append(link.string)
print(pages[-1])  # 마지막 <span class = pn> item을 제외시킴
