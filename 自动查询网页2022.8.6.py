import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
df = pd.read_excel("2022.8.5.xlsx")
print (df.head())
driver = Chrome()
url="https://www.chemicalbook.com/Search.aspx?_s=&keyword="
driver.get(url)
for idx, row in df.iterrows():
    "https://www.chemicalbook.com/Search.aspx?_s=&keyword="
    driver.get(url)
    品名=row["CAS"]
    driver.find_element(By.XPATH, '//*[@id="Keywords"]').send_keys(品名)
    # time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="SearchBtn"]').click()
    time.sleep(1)
    a =  driver.find_element(By.ID, 'mbox')
    print(a.text)
# //*[@id="mbox"]/tbody/tr[2]/td[2]
driver.close()

