from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time 
import pandas as pd

start = time.time()
# Initialize the webdriver
# de manière basique
# driver = webdriver.Chrome()

# avec ChromeDriverManager mieux car update du driver automatiquement
driver = webdriver.Chrome(ChromeDriverManager().install())

# si on a télécharger le driver directement dans le dossier 
# service = Service(executable_path="./chromedriver.exe")
# driver = webdriver.Chrome(service=service)

# Navigate to the website
# driver.get("https://www.billboard.com/charts/hot-100/")
# driver.get("https://www.billboard.com/charts/billboard-global-200/")
driver.get("https://www.billboard.com/charts/billboard-200/")

# Wait for the page to load
# driver.implicitly_wait(10)
time.sleep(10)

# reject all cookies
driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/div[2]/div/div/button[1]").click()

iterateur100 = list(range(1,110,11))
iterateur100.remove(1)

# nb_max 111 ou 221
title,artist,rank,last_week,peak_pos,weeks_on_chart = [],[],[],[],[],[]
allList = [title,artist,rank,last_week,peak_pos,weeks_on_chart]

iterateur200 = list(range(1, 220, 11))
iterateur200.remove(1)

xpath_title = "/html/body/div[4]/main/div[2]/div[3]/div/div/div/div[2]/div[%d]/ul/li[4]/ul/li[1]/h3"
xpath_artist = "/html/body/div[4]/main/div[2]/div[3]/div/div/div/div[2]/div[%d]/ul/li[4]/ul/li[1]/span"
xpath_rank = "/html/body/div[4]/main/div[2]/div[3]/div/div/div/div[2]/div[%d]/ul/li[1]/span "
xpath_last_week = "/html/body/div[4]/main/div[2]/div[3]/div/div/div/div[2]/div[%d]/ul/li[4]/ul/li[4]/span"
xpath_peak_position = "/html/body/div[4]/main/div[2]/div[3]/div/div/div/div[2]/div[%d]/ul/li[4]/ul/li[5]/span"
xpath_weeks_on_chart = "/html/body/div[4]/main/div[2]/div[3]/div/div/div/div[2]/div[%d]/ul/li[4]/ul/li[6]/span"

xpaths = [xpath_title, xpath_artist, xpath_rank, xpath_last_week, xpath_peak_position, xpath_weeks_on_chart]

for week in iterateur200:
    for i, xpath in enumerate(xpaths):
        element = driver.find_element(By.XPATH, xpath % (week))
        allList[i].append(element.text)


# for i, j in zip(allList, allXpath):
#     i = scraper(i,j,iterateur200,221)

df = pd.DataFrame(list(zip(title,artist,rank,last_week,peak_pos,weeks_on_chart)),columns=['Title','Artist','Rank','Last Week','Peak Positon','Weeks on charts'])
print(df)

# Close the webdriver
driver.close()

end = time.time()
temps = end - start
print("temps d'execution :",temps,"s")