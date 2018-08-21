from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import gen4names
import io 

file = io.open("pokemon-gen-4.txt", "w+", encoding='utf8')
file.write("Number, Pokemon, Type1, Type2, HP, Attack, Defense, Speed, Special, PNG".decode('utf8'))
file.write(u'\n')

driver = webdriver.Chrome()
driver.get("https://dex.pokemonshowdown.com/pokemon/")

search_input = driver.find_element_by_class_name("searchbox")
names = gen4names.names

for name in names:
  search_input.clear()
  search_input.send_keys(name)
  search_input.send_keys(Keys.RETURN)
  
  number = driver.find_elements_by_css_selector("code")[0] #includes a hashtag, remove it 
  pokemon = driver.find_elements_by_css_selector(".subtle")[0]
  type1 = driver.find_elements_by_css_selector(".type")[0]
  if len(driver.find_elements_by_css_selector(".type")) == 2:
    type2 = driver.find_elements_by_css_selector(".type")[1]
  else:
    type2 = 'none'
  hp = driver.find_elements_by_css_selector(".stat")[0]
  attack = driver.find_elements_by_css_selector(".stat")[1]
  defense = driver.find_elements_by_css_selector(".stat")[2]
  speed = driver.find_elements_by_css_selector(".stat")[3]
  special = driver.find_elements_by_css_selector(".stat")[5]
  png = driver.find_elements_by_css_selector('.sprite')[0] #take src

  if number:
    file.write(number.text.replace('#', ''))
  file.write(u"\u002C")
  if pokemon:
    file.write(pokemon.text)
  file.write(u"\u002C")
  if type1:
    file.write(type1.text)
  file.write(u"\u002C")
  if type2 != 'none':
    file.write(type2.text)
  file.write(u"\u002C")
  if hp:
    file.write(hp.text)
  file.write(u"\u002C")
  if attack:
    file.write(attack.text)
  file.write(u"\u002C")
  if defense:
    file.write(defense.text)
  file.write(u"\u002C")
  if speed:
    file.write(speed.text)
  file.write(u"\u002C")
  if special:
    file.write(special.text)
  file.write(u"\u002C")
  if png:
    file.write(png.get_attribute('src'))
  file.write(u"\n")

driver.close()

file.close()
