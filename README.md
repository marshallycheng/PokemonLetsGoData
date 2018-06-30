
# PokemonLetsGoData
[Live site](https://marshallycheng.github.io/PokemonLetsGoData/)

PokemonLetsGoData is a data visualization of the first two generations of Pokemon, created with the D3.js library. I've always been a huge fan of the Pokemon series and it's the video game franchise I remember most fondly from my childhood. I imagine that it's the same for many other people from my generation and this project is an opportunity for all of us to enjoy those fond memories. PokemonLetsGoData was built in about 20 hours, and I may or may not come back to this project in the future. 

![Home page](https://i.imgur.com/vYQGs0T.png)

## Features

* Pokemon Details
  * The data display in the top left shows a Pokemon's base stats whenever one is moused over. 
  * PokemonLetsGoData currently features all 251 Pokemon from the first two generations.
* Filters
  * There are filters for the original fifteen types, and filters for the original five base stats.
  * Filtering by type reduces the data set to only show Pokemon that are of that type. Filtering by base stat changes the model size of a Pokemon based on the scale of its corresponding base stat.
  * The first two generations are featured and the generation displayed can be changed at will.
  
## Highlights

### Dynamic Sizing

Every Pokemon has a radius and a collision detector based off its radius. Radiuses are determined as a function of each Pokemon's base stat. When a stat filter is selected, each Pokemon's radius and collision force is updated based on the new stat. Every Pokemon bubble has its data bound to it so that it can update at will without having to be assigned new data.

![Dynamic Sizing](https://i.imgur.com/75xFsts.gif)

#### Default radius and collision based off of Attack
```javascript
// defaulted to center of screen, but leaving forces here in case want to change later. collision is based off of bubble radius
  const simulation = d3.forceSimulation()
    .force("x", d3.forceX().strength(.00000))
    .force("y", d3.forceY().strength(.000))
    .force("collide", d3.forceCollide(function (d) {
      return radiusScale(d.Attack * .9);
    }))
  // radius based off pokemon stat. defaults to attack. fills svg with appropriate pokemon image
  const pokemonBubbles = svgContainer.selectAll('.pokemon-bubble')
    .data(pokemonData)
    .enter().append('circle')
    .attr("class", "pokemon-bubble")
    .attr("r", function (d) {
      return radiusScale(d.Attack);
    })
    .attr("fill", function (d) {
      return `url(#${d.Pokemon})`;
    });
```
#### Size change based on new stat
```javascript
// updates radius and force collision based on selected stat. alpha target and restart allows it to move again
  d3.selectAll('.stat').on('click', function(){
    svgContainer.selectAll('.pokemon-bubble')
      .attr('r', function(d) {
        return radiusScale(d[d3.event.target.value]);
      });
    simulation
      .force("collide", d3.forceCollide(function(d){
        return radiusScale(d[d3.event.target.value] * .9);
      }))
      .alphaTarget(0.25)
      .restart();
  })
```

#### Modifying radius sizes 
```javascript
 // stat will determine size of circle. Defaults to Attack stat, which ranges from 5 to about 140.
    let radiusScale = d3.scaleSqrt().domain([5, 145]).range([10, 46]);
    // dataset defaults to include all pokemon.
    if (type === "all"){
      pokemonData = data;
    } else {
      // filters pokemon based on type. also updates circle radius to take up more of the available space
      pokemonData = data.filter(pokemon => pokemon["Type1"].toLowerCase() === type || 
      pokemon["Type2"].toLowerCase() === type)
      radiusScale = d3.scaleSqrt().domain([5,145]).range([20,100]);
    }
 ```
 
 ### Webscraping
 
 Used Python, [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), and [Selenium](http://selenium-python.readthedocs.io/) to webscrape Generation 2 Pokemon data from [PokemonShowdown](https://pokemonshowdown.com/). BeautifulSoup is a Python library used for extracting data from HTML files. Selenium is a web browsing automator. I used it to navigate to the PokemonShowdown website and type pokemon names into the search bar so BS4 could scrape the necessary data.
 ```python

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

 ```
 
 ## Technologies Used
 
 * Data Visualizaion: D3.js
 * Styling: D3.js/CSS3
 * Data Acquisition: BS4/Selenium
 
 ### Future Features
 
 Features that I'd like to include in the future are as follows:
 * PokeRap singalong
 * More generations
 
