/* 
To check page active url
https://stackoverflow.com/questions/1034621/get-the-current-url-with-javascript
 */

/* 
Multiple conditions 
https://stackoverflow.com/questions/37896484/multiple-conditions-for-javascript-includes-method
*/

// Fire CheckActivePage function when page is loaded
window.onload = function() {
  checkActivePage();
};

/* Check where user is */
function checkActivePage() {

// Grab git page
let gitPage = "https://8080-eb42513f-a0fa-42fd-9fac-02217a4bbd7d.ws-eu01.gitpod.io/"

// Grab active window and set variable activePage
let activePage = window.location.href;

// Categories of recipes
let categories = ["breakfast", "dinner", "lunch", "desserts"];

/* Run the tests against every element in the array
    check if user ulr contain recipe category
    if true line >> 35
*/
let recipePage = categories.some(el => activePage.includes(el));


if (activePage == gitPage ) {
  document.getElementById("home").classList.toggle("visited");
} else if (recipePage == true) {
  document.getElementById("recipe").classList.toggle("visited");
} else if (activePage.includes("index")) {
  document.getElementById("home").classList.toggle("visited");
} else if (activePage.includes("login")) {
  document.getElementById("login").classList.toggle("visited");
} else if (activePage.includes("register")) {
  document.getElementById("register").classList.toggle("visited");
} else if (activePage.includes("my_recipes")) {
  document.getElementById("myRecipes").classList.toggle("visited");
} else if (activePage.includes("add_recipe")) {
  document.getElementById("addRecipe").classList.toggle("visited");
} else if (activePage.includes("edit_recipe")) {
  document.getElementById("myRecipes").classList.toggle("visited");
} else { (activePage.includes("logout")) 
  document.getElementById("logout").classList.toggle("visited");
}

}
