[Main README.md file](README.md)

[View website on Heroku](https://flask-cook-book-project.herokuapp.com/)

* [Browers used in testing](#browers-used-in-testing)
  * [Validators](#validators)
  * [User story testing](#user-story-testing)
      - [Registered Users](#registered-users)
  * [Navigation Bar functionality testing](#navigation-bar-functionality-testing)
  * [Search Bar](#search-bar)
  * [Recipe cards](#recipe-cards)
  * [Add Recipe](#add-recipe)
  * [Edit Recipe](#edit-recipe)
  * [Delete Recipe](#delete-recipe)
  * [Registration and log in / out](#registration-and-log-in---out)
  * [Floating action button](#floating-action-button)

# Manual Testing

- Manual tests have been done throughout the development of the project.
The following test scenarios confirms that the website is behaving accordingly.

## Browers used in testing

- Google Chrome
    - Used for testing site through all developing process and DevTools for    responsiveness and scaling issues on different screen sizes.

- Mozilla Firefox
    - Used for testing site and responsiveness and scaling.

- Opera Web Browser
    - Used for testing site and responsiveness and scaling.

- Microsoft Edge 
    - Used for testing site and responsiveness and scaling.

This was the primary method of testing throughout the development of the project.

## Validators

[**W3C CSS Validator**](https://jigsaw.w3.org/css-validator/) 
- This is online CSS code validator
- All css files pass testing


[**W3C HTML Validator**](https://validator.w3.org/)
- This is online HTML code validator
- All the pages from the site where tested and all the results came back with error on point where jinja templating is used rest of code is validate as valid.
    
[**PEP8 Validator**](http://pep8online.com/)
- This is online Python validator
- Is used to validate python code in app.py
- Code pass validation.


## User story testing

- As a new user, I want to be able to view recipes to cook.
    - **If user click on any recipe card will redirect him to recipe**

- As a new user, I want to be able to search for recipes.
    - **User can search recipes by entering the desirable name of recipe, cooking time, ingredients in search engine** 

- As a new user, I want to be able to easily navigate through the website.
    - **Fixed navigation bar is present at all time to user easily navigate through site**

- As a new user, I want to be able to easily access all of its feature.
    - **User can read and search for recipes for all app feature he needs to register**

- As a new user, I want to be able to immediatly see what the website is about.
    - **With design of page user can immediatly see what this page is about**

- As a new user, I want to be able to see different categories of recipes.
    - **If the user clicks on recipes, he can see different recipe categories, and if scrolls on the home page, he can see 4 recipes from each recipe category..**

- As a new user, I want to be able to know cook time, portion size, prep time or difficulty of recipe. 
    - **Users can easily see this information on a recipe card.**

- As a new user, I want to be able to see whole recipe on separate page
    - **Clicked on the recipe card user gets redirected to a recipe.**

- As a new user, I want to be able to see ingredients needed for dish.
    - **On the recipe page, users can easily see ingredients needed for a recipe.**

- As a new user, I want to be able to see image of dish.
    - **Users can see recipe image on recipe card before he open recipe itself, on mobile screen user can see image directly below recipe information when on bigger devices recipe image is under recipe method.**
- As a new user, I want to be able to create account.

#### Registered Users

- As a returning user, I want to be able to log in to my account easily.
    - **The user can log in to the page through navbar by pressing login or through the home page.**

- As a registered user, I want to be able to create my recipe.
    - **By clicking on add recipe the user is able to add their recipe.**

- As a registered user, I want to be able to see my recipes.
    - **The user can see their recipes on the My recipes page.**

- As a registered user, I want to be able to update my recipe.
    - **The user can edit their recipes by clicking on the edit recipe on my recipes page or through the action button on the recipe page.**

- As a registered user, I want to be able to share my recipes.
    - **At this moment user is not able to share their recipe**

- As a registered user, I want to be able to rate recipes.
    - **At this moment user is not able to rate recipes.**

- As a registered user, I want to be able to see feedback about my recipes.
    - **At this moment user is not able to see feedback about their recipes.**

- As a registered user, I expect my personal details to be private.
    - **User information is safe from stealing**

- As a registered user, I want to be able to delete my account.
    - **At this moment registered user is not able to delete their account.**

## Navigation Bar functionality testing

| Action  | Expetatiopn  | Result |
|---|---|---|
| Clicked **Logo** on Home page  | Refresh **Home** page  | PASS |
| Clicked **Logo** on any other page on site | Return to **Home** page | PASS  |
| Clicked **Home** on Home page  |  Refresh **Home** page | PASS |
| Clicked **Recipes** | Open drop-down menu with categories  | PASS |
| Clicked **Recipes any category**  | Open the desired category | PASS |
| Clicked **Log In / Register**  | Open Log in / Register page | PASS |
| Clicked **My Recipes**  | Open my recipes page  | PASS |
| Clicked **Add Recipes** | Open recipe input page  | PASS  |
| Clicked **Log Out**    | Logged user from page  | PASS  |

## Search Bar

| Action  | Expetatiopn  | Result |
|---|---|---|
| Clicked **Reset** on Home page  | Refresh **Home** page  | PASS |
| Clicked **Reset** on Search page | Return to **Home** page | PASS  |
| Clicked **Search** on Home page  | Display result with message on search  | PASS |
| Clicked **Search** on Search page | Display result with message on search | PASS  |

## Recipe cards 

| Action  | Expetatiopn  | Result |
|---|---|---|
| Clicked **Recipe card** on any page  | Display **Recipe** | PASS |

## Add Recipe

| Action  | Expetatiopn  | Result |
|---|---|---|
| Clicked **Choose Recipe Category**  | Open drop-down menu | PASS |
| Clicked **Choose Recipe Difficulty** |  Open drop-down menu | PASS |
| Clicked **All info buttons**  | Display modal with **Requirements** | PASS |
| **Enter Recipe Name**  by  **Requirements**   | Validate input | PASS |
| **Enter Recipe Name** use just blank spaces | Validate input as wrong | PASS |
| **Enter Recipe Cooking Time**  by  **Requirements**   | Validate input | PASS |
| **Enter Recipe Cooking Time** use just blank spaces | Validate input as wrong | PASS |
| **Enter Recipe Prepare Time**  by  **Requirements**   | Validate input | PASS |
| **Enter Recipe Prepare Time** use just blank spaces | Validate input as wrong | PASS |
| **Enter Recipe Servings**  by  **Requirements**   | Validate input | PASS |
| **Enter Recipe Servings** use just blank spaces | Validate input as wrong | PASS |
| **Recipe Image ULR**  by  **Requirements**   | Validate input | PASS |
| **Recipe Image ULR** use just blank spaces | Validate input as wrong | PASS |
| **Enter recipe ingredients**  by  **Requirements**   | Validate input | PASS |
| **Enter recipe ingredients** use just blank spaces | Validate input as wrong | FAIL |
| **Enter recipe cooking method**  by  **Requirements**   | Validate input | PASS |
| **Enter recipe cooking method** use just blank spaces | Validate input as wrong | FAIL |
| Clicked **Add Recipe** | Added Recipe to db | PASS |

## Edit Recipe

| Action  | Expetatiopn  | Result |
|---|---|---|
| Clicked **Edit on Recipe card** | Open **Edit Recipe** with recipe information | PASS |
| Change any field on **Edit Recipe** and click **Edit Recipe** button | Change and save to db display flash msg | PASS |
| Clicked **Cancel** on edit recipe | Close Edit Recipe and redirect back to My recipes | PASS |

## Delete Recipe

| Action  | Expetatiopn  | Result |
|---|---|---|
| Clicked **Delete** on recipe card  | Display modal with delete question | PASS |
| Clicked **Yes** on modal  | Delete recipe from db and display flash msg | PASS |
| Clicked **No** on modal  | Redirect back to my recipes | PASS |

## Registration and log in / out

| Action  | Expetatiopn  | Result |
|---|---|---|
| Enter username, password and email clicked **Register**  | Register user to db | PASS |
| Enter same username, password and email clicked **Register**  | Display flash msg existing user | PASS |
| Clicked **Log Out** from navbar  | Log out user and Redirect to login | PASS |
| Enter valid username and password on **Log in**  | Logged to my account and display my recipes or msg if no recipes | PASS |
| Enter wrong username or password on **Log in**  | Display flash msg and redirect to login | PASS |


## Floating action button

| Action  | Expetatiopn  | Result |
|---|---|---|
| Clicked **Action button** on any page  | Scroll page on top | PASS |
| Clicked **Action button on Recipe** | Open Action button and display options | PASS |
| Clicked **Back** icon from **Action button** | Redirect to home page | PASS |
| Clicked **Top** icon from **Action button** | Scroll page on top | PASS |
| Clicked **Edit** icon from **Action button** | Open **Edit Recipe** page| PASS |

[Main README.md file](README.md)





