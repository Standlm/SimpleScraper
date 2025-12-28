import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.python.org/jobs/"

page_num = 1
all_jobs = []

while True:
    # Construct URL with page query parameter
    if page_num == 1:
        url = BASE_URL
    else:
        url = f"{BASE_URL}?page={page_num}"

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve page {page_num}")
        break

    soup = BeautifulSoup(response.content, "html.parser")

    # Jobs are listed under ul.list-recent-jobs > li
    job_list = soup.find("ul", class_="list-recent-jobs")
    if not job_list:
        break  # no jobs found, end loop

    jobs = job_list.find_all("li")
    if not jobs:
        break  # no jobs on this page, end loop

    print(f"\n📄 Page {page_num} - Found {len(jobs)} jobs")

    for job in jobs:
        # Job title
        title_tag = job.find("h2")
        title = title_tag.get_text(strip=True) if title_tag else "N/A"

        # Job URL
        link_tag = job.find("a", href=True)
        job_url = "https://www.python.org" + link_tag['href'] if link_tag else "N/A"

        # Company / Location
        company_tag = job.find("span", class_="listing-company-name")
        company = company_tag.get_text(strip=True) if company_tag else "N/A"

        location_tag = job.find("span", class_="listing-location")
        location = location_tag.get_text(strip=True) if location_tag else "N/A"

        job_info = {
            "title": title,
            "company": company,
            "location": location,
            "url": job_url
        }

        all_jobs.append(job_info)

        print(f"Title: {title}")
        print(f"Company: {company}")
        print(f"Location: {location}")
        print(f"URL: {job_url}")
        print("-" * 40)

    page_num += 1  # go to next page

print(f"\n✅ Total jobs collected: {len(all_jobs)}")
