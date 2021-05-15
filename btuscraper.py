

import requests
from bs4 import BeautifulSoup

class BtuScraper:

    URL = "https://btu.edu.ge/ka/contact"

    def scrape_btu(self):
        response = requests.get(self.URL)
        html_tree = BeautifulSoup(response.text , "html.parser")
        btu_divs = html_tree.find_all("div", attrs={"class": "contact_infos"})

        for btu_div in btu_divs:
            print(btu_divs)
            print("*" * 100)
            Address = btu_div.find("div", attrs={"class": "contact_address"}).get_text()
            print("Address -", Address)
            print("*" * 100)
            PhoneNumber = btu_div.find("div", attrs={"class": "contact_telephone"}).get_text()
            print("PhoneNumber -", PhoneNumber)
            print("*" * 100)
            Email = btu_div.find("div", attrs={"class": "contact_email_to"}).get_text()
            print("Email -", Email)
            print("*" * 100)
            MoreInformation = btu_div.find("div", attrs={"class": "contact_moreinformation"}).get_text()
            print("MoreInformation", MoreInformation)
            print("*" * 100)












if __name__ == '__main__':
    btu_scraper = BtuScraper()
    btu_scraper.scrape_btu()