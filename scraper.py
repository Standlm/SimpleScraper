import requests
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com/index.html"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
# First we start by going through every page url and 
books = soup.find_all(class_="product_pod")
for page_num in range(1, 51):  # pages 1–50
    if page_num == 1:
        url = "http://books.toscrape.com/index.html"
    else:
        url = URL.format(page_num)

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    books = soup.find_all("article", class_="product_pod")
    print(f"\n📄 Page {page_num}")
    for book in books:
        title = book.h3.a["title"]                  # already a string
        price = book.find(class_="price_color").get_text()
        availability = book.find(class_="instock availability").get_text(strip=True)

        print(f"Title: {title} | Price: {price} | Availability: {availability}")
        print()
    print(f"{len(books)} books")


