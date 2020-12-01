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
    Display 4 recipe from each category
    Create 4 lists from each recipe category to display on home page
    Find all recipe for each category
    Limit them on 4 entrys from database
    Sort them to show last 4 added in db
    """
    breakfast = {"recipe_category": "Breakfast"}
    breakfast = list(mongo.db.recipes.find(breakfast).limit(4).sort("_id", -1))
    lunch = {"recipe_category": "Lunch"}
    lunch = list(mongo.db.recipes.find(lunch).limit(4).sort("_id", -1))
    dinner = {"recipe_category": "Dinner"}
    dinner = list(mongo.db.recipes.find(dinner).limit(4).sort("_id", -1))
    desserts = {"recipe_category": "Desserts"}
    desserts = list(mongo.db.recipes.find(desserts).limit(4).sort("_id", -1))

    return render_template(
        "pages/index.html", breakfast=breakfast,
        dinner=dinner, lunch=lunch, desserts=desserts)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Search function, use search tutorial from
    Flask Mini-Project 20 | 08 - Searching Within
    The Database (8a - Text Index Searching)
    Offer user to search form db recipes collection 
    all fields category, name ,cook time,etc
    Search use two pages one when user comming from home page
    and one when reset search same page is used
    for display error messages 
     """
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    print(recipes)
    return render_template("pages/search.html", recipes=recipes)


@app.route("/search_all")
def search_all():
    return render_template("pages/search_all.html")


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    """
    Function that finds a specific recipe from db and render it
    to recipe page
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("pages/recipe.html", recipe=recipe)


@app.route('/breakfast')
def breakfast():
    """
    Renders breakfast recipe page and finds all breakfast
    Sort them by last entry in db
    """
    breakfast = {"recipe_category": "Breakfast"}
    breakfast = list(mongo.db.recipes.find(breakfast).sort("_id", -1))
    return render_template(
        "pages/breakfast.html", breakfast=breakfast)


@app.route('/lunch')
def lunch():
    """
    Renders lunch recipe page and finds all lunch
    Sort them by last entry in db
    """
    lunch = {"recipe_category": "Lunch"}
    lunch = list(mongo.db.recipes.find(lunch).sort("_id", -1))
    return render_template(
        "pages/lunch.html", lunch=lunch)


@app.route('/dinner')
def dinner():
    """
    Renders dinner recipe page and finds all dinner
    Sort them by last entry in db
    """
    dinner = {"recipe_category": "Dinner"}
    dinner = list(mongo.db.recipes.find(dinner).sort("_id", -1))
    return render_template(
        "pages/dinner.html", dinner=dinner)


@app.route('/desserts')
def desserts():
    """
    Renders desserts recipe page and finds all desserts
    Sort them by last entry in db
    """
    desserts = {"recipe_category": "Desserts"}
    desserts = list(mongo.db.recipes.find(desserts).sort("_id", -1))
    return render_template(
        "pages/desserts.html", desserts=desserts)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Register functio which check if user is provide uniqe
    username and email if it registration is sucessful
    If not he is returned to try again whit message that something
    is wrong (email or username is aready in db)
    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists!")
            return redirect(url_for("register"))

        # check if email already exists in db
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            flash("Email already exists!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")

        # if register sucessful rediret to My Recipe
        return redirect(url_for("my_recipes", username=session["user"]))
    return render_template("pages/register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exist in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "my_recipes", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("pages/login.html")


@app.route("/my_recipes/<username>", methods=["GET", "POST"])
def my_recipes(username):
    """
    Grab the session user's username from db
    When user is looged, search all recipe added by looged user
    and sort them by last added recipes.
    If log is failed redirect them to login page
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
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        """
        After user add recipe he is redirected to my recipe page
        what give him option to see recipe added and
        process to edit if he make mistake
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
        flash("Recipe Successfully Added")
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
        Edit recipe function
        After user edit own recipe he is redirected
        to page with own recipes
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
    Delete recipe function
    After user delete own recipe he is redirected
    to page with own recipes
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted!")
    return redirect(url_for("my_recipes", username=username))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
