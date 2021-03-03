from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

print("Welcome to the nutrition web scraper!")
query = input("Input a food: ")

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(CHROME_DRIVER_PATH)

driver.get("https://www.nutritionvalue.org/")

search_box = driver.find_element_by_id("food_query")
search_box.send_keys(query)

search_button = driver.find_element_by_xpath('//*[@id="main"]/tbody/tr[3]/td/form/input')
search_button.click()

try:
    driver.find_element_by_xpath('//*[@id="main"]/tbody/tr[4]/td/p[1]')
except NoSuchElementException:

    time.sleep(2)
    url = driver.current_url.replace("#google_vignette", "")
    driver.get(url)

    link = driver.find_element_by_xpath('//*[@id="main"]/tbody/tr[5]/td/table/tbody/tr[2]/td[1]/a')
    food_url = link.get_attribute("href")
    driver.get(food_url)

    time.sleep(2)

    url = driver.current_url.replace("#google_vignette", "")
    driver.get(url)

    time.sleep(2)

    food_name = driver.find_element_by_xpath('//*[@id="main"]/tbody/tr[4]/td/table/tbody/tr[1]/td/h1').text
    calories = driver.find_element_by_xpath('//*[@id="main"]/tbody/tr[4]/td/table/tbody/tr[3]/td[1]/table/tbody/tr/td/table/tbody/tr[5]/td[2]').text
    fat = driver.find_element_by_xpath('//*[@id="main"]/tbody/tr[4]/td/table/tbody/tr[3]/td[1]/table/tbody/tr/td/table/tbody/tr[10]/td[1]').text
    cholesterol = driver.find_element_by_xpath('//*[@id="main"]/tbody/tr[4]/td/table/tbody/tr[3]/td[1]/table/tbody/tr/td/table/tbody/tr[14]/td[1]').text
    carbohydrate = driver.find_element_by_xpath('//*[@id="main"]/tbody/tr[4]/td/table/tbody/tr[3]/td[1]/table/tbody/tr/td/table/tbody/tr[18]/td[1]').text
    protein = driver.find_element_by_xpath('//*[@id="main"]/tbody/tr[4]/td/table/tbody/tr[3]/td[1]/table/tbody/tr/td/table/tbody/tr[24]/td[1]').text

    with open("nutrition_data.csv", "a") as data:
        data.write(f"\n{food_name}, Calories {calories}, {fat}, {cholesterol}, {carbohydrate}, {protein}")


else:
    print("Ho no! We didn't find any results!")
    driver.close()
