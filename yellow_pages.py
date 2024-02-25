import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class YellowPagesScraper:
    def __init__(self) -> None:
        pass

    def scrape(self, url):

        browser = webdriver.Chrome()

        browser.get(url)

        elems = browser.find_elements(By.CLASS_NAME, "result")

        if len(elems) == 0:
            return {"status": "failed", "description": "Result element not found"}

        for i in range(len(elems)):
            elem = elems[i]
            x_path = "./div/div[@class='v-card']/div[@class='info']"

            info = elem.find_element(By.XPATH, x_path)

            primary = info.find_element(
                By.XPATH, "./div[@class='info-section info-primary']"
            )
            secondary = info.find_element(
                By.XPATH, "./div[@class='info-section info-secondary']"
            )

            business_name = primary.find_element(
                By.XPATH, "./h2/a[@class='business-name']/span"
            ).text
            categories = [
                x.text
                for x in primary.find_elements(By.XPATH, "./div[@class='categories']/a")
            ]
            phone = secondary.find_element(
                By.XPATH, "./div[@class='phones phone primary']"
            ).text

            adr = secondary.find_element(By.XPATH, "./div[@class='adr']")
            street_address = adr.find_element(
                By.XPATH, "./div[@class='street-address']"
            ).text
            locality = adr.find_element(By.XPATH, "./div[@class='locality']").text
            address = {"street_address": street_address, "locality": locality}

            data = {
                "business_name": business_name,
                "categories": categories,
                "phone": phone,
                "address": address,
            }

            print(data)


if __name__ == "__main__":
    scraper = YellowPagesScraper()
    url = "https://www.yellowpages.com/search?search_terms=Dentist&geo_location_terms=77079&s=distance&page=2"
    scraper.scrape(url)
