# Import dependencies
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
import datetime
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# Create instance of flask and assign it to "app"
app = Flask(__name__)


# App configuration
# To grab database name
# Connection string
# To grab secret key
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Create instance of PyMongo
mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def home():
    """
    Get all the recipes from the recipe category
    Sort in list by last _id
    Limit to four
    Render recipe category on index.html
    """
    breakfast = {"recipe_category": "Breakfast"}
    breakfast_sort = list(
        mongo.db.recipes.find(breakfast).limit(4).sort("_id", -1))
    lunch = {"recipe_category": "Lunch"}
    lunch_sort = list(
        mongo.db.recipes.find(lunch).limit(4).sort("_id", -1))
    dinner = {"recipe_category": "Dinner"}
    dinner_sort = list(
        mongo.db.recipes.find(dinner).limit(4).sort("_id", -1))
    desserts = {"recipe_category": "Desserts"}
    desserts_sort = list(
        mongo.db.recipes.find(desserts).limit(4).sort("_id", -1))

    return render_template(
        "pages/index.html", breakfast=breakfast_sort,
        dinner=dinner_sort, lunch=lunch_sort, desserts=desserts_sort)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Search function, use search tutorial from
    Flask Mini-Project 20 | 08 - Searching Within
    The Database (8a - Text Index Searching)
    A function that finds recipes on query
    The query is the user's input
    Recipes are a list of user queries
    Render user's list recipes on search.html
    """
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("pages/search.html", recipes=recipes)


@app.route("/new_search")
def new_search():
    # A function that start new search
    # Render search on new_search.html
    return render_template("pages/new_search.html")


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    """
    A function that finds only one recipe by recipe id
    Renders only one recipe on recipe.html
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("pages/recipe.html", recipe=recipe)


@app.route('/breakfast')
def breakfast():
    """
    A function that finds all recipes in the recipe category
    The breakfast is a list of recipes sorted by last _id
    Renders them in breakfast.html
    The following three functions apply the same logic
    """
    breakfast = {"recipe_category": "Breakfast"}
    breakfast = list(mongo.db.recipes.find(breakfast).sort("_id", -1))
    return render_template(
        "pages/breakfast.html", breakfast=breakfast)


@app.route('/lunch')
def lunch():
    lunch = {"recipe_category": "Lunch"}
    lunch = list(mongo.db.recipes.find(lunch).sort("_id", -1))
    return render_template(
        "pages/lunch.html", lunch=lunch)


@app.route('/dinner')
def dinner():
    dinner = {"recipe_category": "Dinner"}
    dinner = list(mongo.db.recipes.find(dinner).sort("_id", -1))
    return render_template(
        "pages/dinner.html", dinner=dinner)


@app.route('/desserts')
def desserts():
    desserts = {"recipe_category": "Desserts"}
    desserts = list(mongo.db.recipes.find(desserts).sort("_id", -1))
    return render_template(
        "pages/desserts.html", desserts=desserts)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    A function that check user input and register user in db
    An existing_user is a register user
    An existing_email is a register email
    If the user's username form input is an existing_user
    Flash message and redirect to register.html
    If the user's email form input is an existing_email
    Flash message and redirect to register.html
    If the register user is not existing_user
    Get register user username, email and password
    Salt register password for security and
    Insert one register user in db
    Flash message and redirect to my_recipes.html
    The registered user is saved in the session by username
    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists!")
            return redirect(url_for("register"))

        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            flash("Email aready in use! Please try again")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")

        return redirect(url_for("my_recipes", username=session["user"]))
    return render_template("pages/register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
A Function that finds one existing_user in db
Get its username from the user's username form input
If checks_password_hash get existing_user password
Flash message and redirect to my_recipes.html
Else flash message and redirect to login.html
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "my_recipes", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("pages/login.html")


@app.route("/my_recipes/<username>", methods=["GET", "POST"])
def my_recipes(username):
    """
    A function that find all recipes
    created_by logged_user session username
    If session user render my_recipes.html and
    find my_recipes from logged_user username
    Sort them by _id by last added recipe
    If not redirect to login
    """
    logged_user = {"created_by": username}
    my_recipes = mongo.db.recipes.find(logged_user).sort("_id", -1)
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template(
            "pages/my_recipes.html", username=username, my_recipes=my_recipes)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    A Function that pop user from session
    And redirect user to login.html
    """
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        """
        Function that if request method is post
        Finds the recipe category and recipe difficulty
        Render them to add_recipe.html and
        Find one user username from the session
        Inserts one recipe into the db and save user session username
        In the recipe created_by and save today now in date_created
        Flash message and redirect to my_recipes.html
        If not render username my_recipes.html
        """
        today = datetime.datetime.now()

        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        recipe = {
            "recipe_category": request.form.get("recipe_category"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_cooking_time": request.form.get("recipe_cooking_time"),
            "recipe_prep_time": request.form.get("recipe_prep_time"),
            "recipe_servings": request.form.get("recipe_servings"),
            "recipe_difficulty": request.form.get("recipe_difficulty"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "created_by": session["user"],
            "date_created": today.strftime("%d/%m/%Y, %H:%M:%S")
        }

        mongo.db.recipes.insert_one(recipe)
        flash(
            "Thank you for adding the recipe and for using the"
            "Cook Book app.You can find your recipes below,"
            "the last recipe added is always in the first place!")
        return redirect(url_for("my_recipes", username=username))

    categories = mongo.db.categories.find()
    difficultys = mongo.db.difficulty.find()
    return render_template(
         "pages/add_recipe.html",
         categories=categories, difficultys=difficultys)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        """
        Function that if request method is post
        Finds one recipe by _id from db
        And by the user username from the session
        Find recipe category and recipe difficulty
        Render recipe to edit_recipe.html and
        Update recipe by user form input
        Update date_created with today
        Flash message and redirect to my_recipes.html
        If not render edit_recipe.html
        """
        today = datetime.datetime.now()

        submit = {
            "recipe_category": request.form.get("recipe_category"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_cooking_time": request.form.get("recipe_cooking_time"),
            "recipe_prep_time": request.form.get("recipe_prep_time"),
            "recipe_servings": request.form.get("recipe_servings"),
            "recipe_difficulty": request.form.get("recipe_difficulty"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "created_by": session["user"],
            "date_created": today.strftime("%d/%m/%Y, %H:%M:%S")
        }

        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")
        return redirect(url_for("my_recipes", username=username))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    difficultys = mongo.db.difficulty.find()
    return render_template(
            "pages/edit_recipe.html", recipe=recipe,
            categories=categories, difficultys=difficultys)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    Function that find one the user in the session
    And remove recipe by recipe_id
    Flash message and redirect to username my_recipes
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted!")
    return redirect(url_for("my_recipes", username=username))


if __name__ == "__main__":
    """ DEBUG SET TO FALSE BEFORE SUBMIT PROJECT """
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
