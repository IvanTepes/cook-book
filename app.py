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
    # Display 4 recipe from each category
    breakfast = {"recipe_category": "Breakfast"}
    breakfast = list(mongo.db.recipes.find(breakfast).limit(4).sort("_id", -1))
    lunch = {"recipe_category": "Lunch"}
    lunch = list(mongo.db.recipes.find(lunch).limit(4).sort("_id", -1))
    dinner = {"recipe_category": "Dinner"}
    dinner = list(mongo.db.recipes.find(dinner).limit(4))
    desserts = {"recipe_category": "Desserts"}
    desserts = list(mongo.db.recipes.find(desserts).limit(4))

    return render_template(
        "/index.html", breakfast=breakfast,
        dinner=dinner, lunch=lunch, desserts=desserts)


@app.route("/register", methods=["GET", "POST"])
def register():
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
        return redirect(url_for("profile", username=session["user"]))
    return render_template("/register.html")


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
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

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
        # Convert user input array list into string and save to db
        # https://www.decalage.info/en/python/print_list
        allergen_list = request.form.getlist("recipe_allergen")
        today = datetime.datetime.now()

        recipe = {
            "recipe_category": request.form.get("recipe_category"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_cuisine": request.form.get("recipe_cuisine"),
            "recipe_cooking_time": request.form.get("recipe_cooking_time"),
            "recipe_allergen": ', '.join(allergen_list),
            "recipe_size": request.form.get("recipe_size"),
            "recipe_difficulty": request.form.get("recipe_difficulty"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "created_by": session["user"],
            "date_created": today.strftime("%d/%m/%Y, %H:%M:%S")
        }

        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("add_recipe"))

    categories = mongo.db.categories.find()
    allergens = mongo.db.allergens.find().sort("allergens_name", 1)
    difficultys = mongo.db.difficulty.find()
    return render_template(
        "add_recipe.html", categories=categories,
        allergens=allergens, difficultys=difficultys)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
