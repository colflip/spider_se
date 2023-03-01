import csv
import requests
from bs4 import BeautifulSoup

def get_baidu_search_results(query):
    url = "https://www.baidu.com/s?wd=" + query
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find_all("div", class_="result c-container")
    titles_and_links = []
    for result in results:
        title_element = result.find("h3")
        if title_element is None:
            continue
        title = title_element.text
        link_element = result.find("a")
        if link_element is None:
            continue
        link = link_element["href"]
        titles_and_links.append((title, link))
    return titles_and_links

query = "bilibili"
titles_and_links = get_baidu_search_results(query)

with open("search_results.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Link"])
    for title, link in titles_and_links:
        writer.writerow([title, link])
