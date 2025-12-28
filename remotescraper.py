import requests
from bs4 import BeautifulSoup

URL = "https://remote.co/remote-jobs/developer"
response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

# Each job listing div has class "sc-dvmKnY hvxynC"
jobs = soup.find_all("div", class_="sc-dvmKnY hvxynC")

for job in jobs:
    # Job title
    title_tag = job.find("span", class_="sc-brCpQf czmbDP")
    title = title_tag.get_text(strip=True) if title_tag else "N/A"

    # Posted time
    time_tag = job.find("span", class_="sc-cZwzVE kmPMrx")
    posted_time = time_tag.get_text(strip=True) if time_tag else "N/A"

    # Job URL
    link_tag = job.find("a", href=True)
    job_url = "https://remote.co" + link_tag['href'] if link_tag else "N/A"

    # Job type / work mode
    li_tags = job.find_all("li", class_="sc-evFSHL hVyzR")
    job_types = [li.get_text(strip=True) for li in li_tags]

    # Location
    location_tag = job.find("span", class_="sc-fxAWvV iGCdGL")
    location = location_tag.get_text(strip=True) if location_tag else "N/A"

    print(f"Title: {title}")
    print(f"Posted: {posted_time}")
    print(f"URL: {job_url}")
    print(f"Type: {', '.join(job_types)}")
    print(f"Location: {location}")
    print()
