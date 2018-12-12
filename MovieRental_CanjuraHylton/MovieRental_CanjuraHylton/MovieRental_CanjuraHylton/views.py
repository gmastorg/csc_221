"""
Routes and views for the flask application.
"""

import os
from MovieRental_CanjuraHylton import login
from MovieRental_CanjuraHylton import rentReturn
from MovieRental_CanjuraHylton import listBuilder
from MovieRental_CanjuraHylton import rentals
from MovieRental_CanjuraHylton import store
from datetime import datetime
from flask import render_template
from MovieRental_CanjuraHylton import app
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import login_user, LoginManager, UserMixin, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

comments = []
allMovies = [] 
movies = []
cart = []

selectedMovie =""
selectedFormat = ""
s = store.Store()

app.config["DEBUG"] = True

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message=s.message,
        store = s.name,
        address = s.address,
        city = s.city,
        state = s.state,
        zip = s.zipcode,
        hours = s.hours,
        phone = s.phone
          )

@app.route('/about', methods = ["GET", "POST"])
def about():
    """Renders the about page. reads comments from file and displays them saves new comments to file"""
    comments = listBuilder.getComments()

    if request.method == "GET":
        return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='We are a video rental store. We have several movies for you to enjoy.',
        comments = comments
        )

    if request.method == "POST":
        comments.append(request.form["contents"])
        saveComments(request.form["contents"])
        return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='We are a video rental store. We have several movies for you to enjoy.',
        comments = comments
        )
      
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", error=False)
    if request.method == "POST":
        username = request.form["username"]
        if username is "":
            return render_template("login.html", error=True)
        if login.login(username, request.form["password"]) == False:
            return render_template("login.html", error=True)
        else: #If the password matches, log the user in
            customerLogin = validate.getFileName(username)
            customer = login.getCustomerInfo(customerLogin)
            return render_template(
                        "index.html",)
                        


#@app.route('/login', methods = ["GET"])
#def login():
  # """Renders the login page. Login itself not yet functioning"""
#    return render_template(
 #       'login.html',
  #   year=datetime.now().year,
    #    message='Login to rent or return a movie.',
     #   username = request.args.get('type'),
      #  password = request.args.get('type')
    #)
    #redirect(url_for('login'))

@app.route('/movies', methods = ["GET", "POST"])
def movies():
    """Renders the movies page."""
    allMovies=listBuilder.getAllMovieTitles()
    return render_template(
        'movies.html',
        title='Movies',
        year=datetime.now().year,
        message='Select from one of our many movies below:',
        allMovies = allMovies,
    )  

    redirect(url_for('movies'))

@app.route('/checkout', methods = ["GET", "POST"])
def checkout():
    """Renders the checkout page. Has cart and total form to pay not functioning yet."""
    selectedMovie = request.args.get('type'),
    selectedFormat = request.args.get('format')
    cart = getCart(selectedMovie, selectedFormat)
    cartsize = len(cart)
    total = getTotal(cart)
    tax = 1.05
    grandtotal = (total*tax)
    days = 3
    return render_template(
        'checkout.html',
        title='Checkout',
        year=datetime.now().year,
        message='Let us Checkout.',
        cart = cart,  
        cartsize = cartsize,
        days = days,
        total = '{0:.2f}'.format(total),
        tax = '{0:.2f}'.format(grandtotal-total),
        grandtotal = '{0:.2f}'.format(grandtotal),
    )
    redirect(url_for('checkout'))

@app.route('/returns')
def returns():
    """Renders the returns page. Not yet fully functioning"""
    return render_template(
        'returns.html',
        title='Return',
        year=datetime.now().year,
        message='Return outstanding movies.'
    )

@app.route('/logout')
def logout():
    """Renders the returns page. Not yet fully functioning"""
    return render_template(
        'logout.html',
        title='Logout',
        year=datetime.now().year,
        message='You are logged out.'
    )

def getCart(selectedMovie, selectedFormat):

    movies = listBuilder.getMovieLists()    
    selectedMovie = selectedMovie[0]
    for item in movies:
        print("comparing",selectedMovie,"with",item.title)
        if selectedMovie == item.title:
          rental = rentReturn.getRateAndFormat(item, selectedFormat)   
          cart.append(rental)

    return cart

def getTotal(cart):

    total = 0    

    for item in cart:
        total += item.rate*3
    
    return total

def saveComments(comment):

    outfile = open(os.path.dirname(__file__)+"/CSVFiles/comments.csv", 'a')
    
    outfile.write(comment+",\n")
    
    outfile.close()