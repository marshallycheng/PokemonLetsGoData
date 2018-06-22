## PokemonLetsGoData - A journey through the world of Pokemon data

### Background and Overview

Pokemon as a franchise is one of the most iconic and successful series in gaming. With 7 full generations(and an 8th in the works), there are over 700 unique pokemon, each with their own set of stats and moves. 

With this project, my goal is to create a data visualization of various pokemon data, starting with base stats across individual pokemon species and adding more categories and selectors as the project grows. 

Users will be able to check various selectors to modify the data and be able to view it in different ways or to fulfill different purposes for themselves. Additionally, users will be able to mouse over individual pokemon images(bubbles) and view more detailed information about that particular pokemon. 

### Functionality and MVP

With PokemonLetsGoData, users will be able to:
- View data on pokemon statistics as they relate to one another between large groups.
- View individual data on a particular pokemon species.
- Check selectors that modify parameters specifying what data should be shown and across which groups.

In addition, the project will include:
- A primer that describes functionality and what data exists in Pokemon.

### Wireframes

The app will consist of a single screen with a pokemon-themed background, a main section showing the data visualization, sidebar selectors to filter data, links to my Github and Linkedin, and an About section.

Possible filters will include which pokemon generations to display, and also filters based on pokemon types.
In the main section, users can mouse over a pokemon image(bubble) to display additional information. 

![Pokemon wireframe](https://github.com/marshallycheng/PokemonLetsGoData/blob/master/pokemon-js-wireframe.png)

### Architecture and Technologies

This project will be implemented with the following technologies:
- D3 for overall structure and DOM manipulation and some styling
- CSS for the remainder of the styling
- Vanilla javascript for general logic

In addition to webpack, there will be a number of scripts involved:

`display.js`: File handling all logic related to styling and organizing displays.

`logic.js`: File encompassing additional logic that may be required, such as code for avoiding collisions between bubbles.

### Implementation Timeline

**Over the Weekend:**

- [x] Acquire csv files for pokemon data
- [x] Begin learning D3 and understanding how to use it for the scope of the project

**Day 1:** Setup necessary node modules, get webpack up and running. Create webpack.config.js and package.json. Write a basic entry file and finish prep for D3. 
Goals for the day:
- [x] Get webpack serving files and frame out index.html
- [x] Understand d3 enough to actually be able to render some default graphs

**Day 2** Improve understanding of d3 and begin displaying pokemon as bubbles on the graph and be able to organize them according to some type of filter. Start working on logic for displaying different sets of data
Goals for the day:
- [x] Display bubbles in some type of order
- [x] Start writing logic for different filters

**Day 3** Finish or come close to finishing the logic for displaying groups of different data. Write out functions for collision and also handling different size data sets.
Goals for the day:
- [x] Finish logic for displaying different groups data.
- [x] Write collision logic and dynamic functions that handle different amounts of data.

**Day 4** Create styling for different groups based on things like typing. Style the frontend, make everything look polished. 
Goals for the day:
- [x] Implement checkboxes for filters.
- [x] Write about section and style the page.
- [x] Make sure everything looks nice.

### Bonus Features
- [ ] Additional filters
- [x] More generations of pokemon
- [ ] Alternate data views
- [ ] Better styling
- [ ] Pokerap?
