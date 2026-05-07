from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

with open("ssge_apartments.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["სათაური", "ფასი"])

    for page in range(1, 4):
        driver.get(f"https://ss.ge/ka/udzravi-qoneba/l/bina/iyideba?page={page}")
        time.sleep(3)

        titles = driver.find_elements(By.TAG_NAME, "h2")
        prices = driver.find_elements(By.CLASS_NAME, "gCRohU")

        for title, price in zip(titles, prices):
            writer.writerow([title.text, price.text])

        print(f"გვერდი {page} - {len(titles)} განცხადება")

driver.quit()
print("მზადაა!")