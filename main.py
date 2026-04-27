from this import d
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from fake_useragent import UserAgent
import time

options = Options()
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option(
    'prefs', {'profile.managed_default_content_settings.media_stream': 2}
)
options.add_argument('--start-maximized')
options.add_argument('--disable-infobars')
#options.add_argument('--disable-extensions')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1920,1200')
options.add_argument('--start-fullscreen')
options.add_argument('--mute-audio')
options.add_extension('./ublock.crx')
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument('--disable-notifications')
options.add_argument(
    '--disable-features=PreloadMediaEngagementData,MediaEngagementBypassAutoplayPolicies'
)
options.add_argument('--autoplay-policy=user-required')
ua = UserAgent()
user_agent = ua.random
options.add_argument(f"user-agent={user_agent}")

monpilote = webdriver.Chrome(options=options)
print('Chrome démarré')

monpilote.get('https://openlibrary.org/')

livre = 'aventure'

mazonelivre = monpilote.find_element(By.XPATH,'//*[@id="header-bar"]/div[2]/div/div[1]/form/input[1]')

mazonelivre.send_keys(livre)
mazonelivre.send_keys(Keys.ENTER)

listZoneTitre = WebDriverWait(monpilote, timeout=3).until(expected_conditions.presence_of_all_elements_located ((By.XPATH, '//*[@id="searchResults"]/ul/li[*]/div/div[1]/div[1]/h3/a')))
b = []
b.append( ['Titre'] )
for x in listZoneTitre :
  Titre = x.text
  print(Titre)
  if Titre != "" :
    r = [ Titre ]
    b.append( r )
      
listZoneAuteur = WebDriverWait(monpilote, timeout=3).until(expected_conditions.presence_of_all_elements_located ((By.XPATH, '//*[@id="searchResults"]/ul/li[*]/div/div[1]/span[1]/a')))
a = []
a.append( ['Auteur'] )
for x in listZoneAuteur:
  Auteur = x.text
  print(Auteur)
  if Auteur != "" :
    r = [ Auteur ]
    a.append( r )

listZoneEditions = WebDriverWait(monpilote, timeout=3).until(expected_conditions.presence_of_all_elements_located ((By.XPATH, '//*[@id="searchResults"]/ul/li[*]/div/div[1]/div[2]/span[2]/span[2]/a')))
c = []
c.append( ['Editions'] )
for x in listZoneEditions :
  Editions = x.text
  print(Editions)
  if Titre != "" :
    r = [ Editions ]
    c.append( r )

e = []
for i in range(len(b)):
  x=b[i][0]
  y=a[i][0]
  z=c[i][0]
  r = [x, y, z]
  e.append(r)

print(e)

import csv
fichier = open("library.csv", "w")
écrivain = csv.writer(fichier, delimiter=",")
écrivain.writerows( e )
fichier.close()
input("Presser une touche pour quitter...")