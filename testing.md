# Manual Testing

- Manual tests have been done throughout the development of the project.
The following test scenarios confirms that the website is behaving accordingly

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








