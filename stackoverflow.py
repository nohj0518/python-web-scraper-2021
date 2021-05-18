import requests
from bs4 import BeautifulSoup

# URL = f"https://stackoverflow.com/jobs?q=python"

# 찾고 싶은 word가 매번 달라지기 때문에
# 요청을 보낼 url도 매번 달라진다
# url에 넣을 word를 main에서 받아왔고 해당 word에 대한 url을
# get_jobs에서 매번 만들어 요청해 줄 수 있도록 구현


# Step 1 get the pages
# Step 2 make requests
# Step 3 extract jobs


def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", class_="s-pagination").find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


def extract_job(html):
    title = html.find("h2", {"class": "mb4"}).find("a")["title"]
    company, location = html.find("h3", {"class": "mb4"}).find_all(
        "span", recursive=False
    )
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)
    job_id = html["data-jobid"]
    return {
        "title": title,
        "company": company,
        "location": location,
        "apply_link": f"https://stackoverflow.com/jobs/{job_id}",
    }


def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping SO page {page}.")
        result = requests.get(f"{url}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs(word):
    url = f"https://stackoverflow.com/jobs?q={word}"
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url)
    return jobs
