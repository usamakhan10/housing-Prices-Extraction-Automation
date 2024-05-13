from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#scraping
prices = []
addresses = []
links = []
print(f"Extracting the prices from webpages")
for page_number in range(1,20):
    response = requests.get(url=f"https://www.zameen.com/Homes/Lahore-1-{page_number}.html?price_max=20000000&area_min=104.51592000000001")
    soup = BeautifulSoup(response.text, features="html.parser")

    price_response = soup.find_all("span" , class_="f343d9ce")
    address_response = soup.find_all("div" , class_="_162e6469")
    link_response = soup.find_all("a" , class_="_7ac32433")

    for result in range(len(price_response)):
        prices.append(price_response[result].getText())
        addresses.append(address_response[result].getText())
        links.append(link_response[result].get("href"))
  

print("launching chrome to enter all data into google forms")

#automation
driver = webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSe38ewI-SHWs-k8HFoGOf8nXPLXEmiGms7BUij19qG0vOLpIg/viewform?usp=sf_link")
driver.maximize_window()

time.sleep(5)
for i in range(len(prices)):
    time.sleep(3)
    all_inputs = driver.find_elements(By.CLASS_NAME , "whsOnd.zHQkBf")
    #entering price
    all_inputs[0].send_keys(prices[i])

    #entering address
    all_inputs[1].send_keys(addresses[i])

    #entering links
    all_inputs[2].send_keys(links[i])

    #submiting
    submit_button = driver.find_element(By.CLASS_NAME , "uArJ5e.UQuaGc.Y5sE8d.VkkpIf.QvWxOd")
    submit_button.click()

    time.sleep(3)

    #refreshing page
    driver.refresh()



