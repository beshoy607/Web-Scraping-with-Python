#selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

chrome_options = Options()
chrome_options.add_argument("no-sandbox")
chrome_options.add_argument("disable-gpu")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

query = "iphones"
url = f"https://en.wikipedia.org/w/index.php?search={query}"
driver.get(url)

time.sleep(10)

soup = BeautifulSoup(driver.page_source, "html.parser")
items = soup.find_all("div", class_="mw-search-result")

print(" All Wikipedia Search Results")
for item in items:
    title = item.find("a")
    description = item.find("div", class_="searchresult")
    if title:
        desc_text = description.text.strip() if description else "No description"
        print(f" {title.text} - {desc_text}")

driver.quit()