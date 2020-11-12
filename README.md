# Cook Book

Cook Book is site for all gourmets and people who love to cook, share, try a new recipes and delicious food. Cook Book offers the user a quick and effective way to get the desired specific recipe in the fastest possible way.

## UX

### Goals

The central target audience for Cook Book are people:

- Who are old enough to be able to use household appliances on their own, who possess a certain level of skill to operate this type of tool.
- Who like to share recipes and knowledge about food and be part of this type of community.

User Goal are:

- Find recipe on fastest posible way.
- Find important information about recipe without too much looking.
- Share recipes with community. 

Cook Book is a great way to help users meet these needs because:

- The planning and design process took all these needs into account before starting to build it.
- The needs of the user may vary and vary from person to person and this site tries to cover some of the most important issues that the user    has when visiting this site such as: 
    - Time need to cook dish
    - Size of dish
    - Possible allergens
    - Skill needed
- Cook Book allows registered users to share their best creations with the community in form of CRUD operations (create, read, update, delete)

### User Stories

#### New Users

- As a new user, I want to be able to view recipes to cook.
- As a new user, I want to be able to search for recipes.
- As a new user, I want to be able easily navigate through the website. 
- As a new user, I want to be able to easily access all of its feature.
- As a new user, I want to be able to immediatly see what the website is about.
- As a new user, I want to be able to see different categories of recipes.
- As a new user, I want to be able to know cook time, portion size, allergens or difficulty of dish. 
- As a new user, I want to be able to see whole recipe on separate page
- As a new user, I want to be able to see ingredients needed for dish.
- As a new user, I want to be able to see image of dish.
- As a new user, I want to be able to create account.

#### Registered Users

- As a returning user, I want to be able to log in to my account easily.
- As a registered user, I want to be able to create my recipe.
- As a registered user, I want to be able to see my recipes.
- As a registered user, I want to be able to update my recipe.
- As a registered user, I want to be able to share my recipes.
- As a registered user, I want to be able to rate recipes.
- As a registered user, I want to be able to see feedback about my recipes.
- As a registered user, I expect my personal details to be private.
- As a registered user, I want to be able to delete my account.

### Design Choices

#### Fonts

Two fonts were used in this project.

- [Pacifico](https://fonts.google.com/specimen/Pacifico)
    - The Pacifico font is used for document headers because it resembles a handwritten one and the page gets the impression of a book.

- [Roboto](https://fonts.google.com/specimen/Roboto?query=Roboto)
    - The Roboto font was used for all other parts of the page where text was used and because it blends in nicely with the rest of the page.

#### Icons

All icons used were chosen for their obvious meaning and purpose so that they can be understood by everyone.

#### Colours

The color palette contains two dark, two light and one bright color. Combining these colors I got an eye-pleasing and interesting look.

#### Styling

- Cards and container boxes were given rounded corners with shadows.
- Repeating the same rounded corner pattern throughout the page keeps consistency in design and maintains the feeling that all elements         belong together.
- Pictures that accurately show the finished result of the recipes.
- SHADOWS?
- BUTTONS?
- HOVER?
- DIVIDERS?

### Wireframes

These wireframes were created using [Balsamiq](https://balsamiq.com/) during the Scope Plane part of the design and planning process for this project.

- Wireframes for this project can be found [here](readme_files/wireframes/cook_book_wireframes.pdf).
- Colored wireframes can be found [here](readme_files/wireframes/colored_wireframes/cook_book_wireframes_colored.pdf).

#### Entity Relationship Diagram

For creating ERD i used [**LucidChart**](https://lucid.app/) during the Scope Plane part of the design and planning process for this project.

- ERD can be found [here](readme_files/erd_diagram/cook-book-erd.png).


## Features

### Existing Features

#### Navigation Bar

- Allows all users to select the content they want to view by simply clicking them, this also collapses into a toggle on mobile devices to.
- After the user registers, the navigation bar expands and gets two new items My Recipes and Add Recipe.  

#### Search Bar

- So the user can find recipes
- The user can find the search bar on the home page and on the pages where the recipes are grouped as Dinner, giving the user the option to     continue searching for recipes without returning to the home page.

#### Parallax Hero Image
- 
#### Return Button 

- Allow user a quick return to the Home page.

#### Quick Log In

- Allow the user a quick login to his account directly from the home page.

#### Recipe Cards

- Allow the user to see without searching and clicking the recipe they would like, also providing the user with more important information      about the recipe.

#### Allergens Guide

#### Log In / Register Page

- Allows a new user to create their account and allows existing users to log in to their account.

#### My Recipes

- Allows registered users to **view** previously added recipe.
- Allows registered users to **update** their recipe.
- Allows registered users to **delete** their recipe. 

#### Add Recipe

- Allows registered users to add their own recipes.

#### Footer 

### Features Left to Implement

#### Rate Recipe 
#### Admin Statistics

## Technologies Used
- [**HTML**](https://www.w3.org/TR/html52/)
    - standard markup language for creating Web pages.
- [**CSS**](https://www.w3.org/Style/CSS/Overview.en.html)
    - to describe and style HTML document such as layout, colors, font and animation.
- [**Github**](https://github.com/)
    - to store and share all project code remotely.
- [**Gitpod**](https://gitpod.io/)
    - used as development environment for building the application.
- [**MongoDB Atlas**](https://www.mongodb.com/cloud/atlas)
    - used for database storage
- [**Trello**](https://trello.com/)
    - to save and organize user stories.
- [**Monday.com**](https://monday.com/)
    - for organizing and planning the project and its phases.
- [**Google Fonts**](https://fonts.google.com/)
    - to style the website fonts.
- [**Materialize**](https://materializecss.com/index.html)
    - to simplify the structure of the website and make the website responsive easily.
- [**Balsamiq Wireframes**](https://balsamiq.com/wireframes/)
    - to create the wireframes and planning this project.
- [**Photoshop**](https://www.adobe.com/ie/products/photoshop.html)
    - to edit, crop and save images as well as logo creator.
- [**Dev Tools**](https://developers.google.com/web/tools/chrome-devtools)
    - to keep track and test the code during the development.
- [**Tinypng**](https://tinypng.com/)
    - to compress the size of the images.
- [**Coolors**](https://coolors.co/)
    - used to choose color pattern.
- [**JQuery**](https://jquery.com/)
    - to simplify DOM manipulation and **Materialize** initalization.
- [**Flask**](https://flask.palletsprojects.com/en/1.0.x/)
    - to construct and render pages.
- [**Jinja**](https://jinja.palletsprojects.com/en/2.10.x/)
    - to simplify displaying data from the backend of this project smoothly and effectively in html.
- [**PIP**](https://pip.pypa.io/en/stable/installing/)
    - for installation of tools needed in this project.
- [**PyMongo**](https://pymongo.readthedocs.io/en/stable/)
    - to make communication between Python and MongoDB possible.
- [**Favicon.io**](https://favicon.io/favicon-converter/)
    - to create Favicon.
- [**LucidChart**](https://lucid.app/)
    - to create ERD (Entity Relationship Diagram)
## Testing

- Testing information can be found in separate testing.md file.

## Deployment

## Credit
### Content

#### Recipes

### Media
### Acknowledgements