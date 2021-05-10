import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://indeed.com/jobs?q=python&limit={LIMIT}&start=99999"


def extract_indeed_pages():
    # soup 은 데이터 추츨하는 역할

    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", class_="pagination")

    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]:
        pages.append(link.string)
    max_page = int(pages[-1])  # 마지막 <span class = pn> item을 제외시킴

    return max_page


def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    company = company.strip()
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    # div에 접근하고 [data-rc-loc]라는 attribute에 접근한 것
    job_id = html["data-jk"]

    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"https://www.indeed.com/viewjob?jk={job_id}&from=serp&vjs=3",
    }


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page}.")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs
