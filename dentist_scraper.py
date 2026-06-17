from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

search_query = "Dentist in Hyderabad"
url = f"https://www.google.com/maps/search/{search_query.replace(' ', '+')}"
driver.get(url)
time.sleep(7)

scrollable_div = driver.find_element(By.CSS_SELECTOR, 'div[role="feed"]')
for i in range(25):
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)
    time.sleep(4)

data = []
results = driver.find_elements(By.CSS_SELECTOR, 'a.hfpxzc')

for result in results:
    try:
        driver.execute_script("arguments[0].click();", result)
        time.sleep(5)
        
        try: name = driver.find_element(By.CSS_SELECTOR, 'h1.DUwDvf').text
        except:
            try: name = driver.find_element(By.CSS_SELECTOR, 'h1').text
            except: name = "N/A"
        
        try: website = driver.find_element(By.CSS_SELECTOR, 'a[data-item-id="authority"]').get_attribute("href")
        except: website = "N/A"
            
        try: phone = driver.find_element(By.CSS_SELECTOR, 'button[data-item-id*="phone"] div.fontBodyMedium').text
        except: phone = "N/A"
            
        try: address = driver.find_element(By.CSS_SELECTOR, 'button[data-item-id="address"] div.fontBodyMedium').text
        except: address = "N/A"
            
        try: rating = driver.find_element(By.CSS_SELECTOR, 'div.F7nice span[aria-hidden="true"]').text
        except: rating = "N/A"

        # Email కోసం లాజిక్
        try:
            email = driver.find_element(By.CSS_SELECTOR, 'a[href^="mailto:"]').text
        except:
            email = "N/A"
        
        data.append({
            "Business Name": name,
            "Website Name": website,
            "Phone": phone,
            "Address": address,
            "Rating": rating,
            "Email": email
        })
    except:
        continue

df = pd.DataFrame(data)
df.to_csv("All_Dentists_Hyderabad_With_Email.csv", index=False)
driver.quit()