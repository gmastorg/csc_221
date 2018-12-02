"""
Routes and views for the flask application.
"""

from MovieRental_CanjuraHylton import listBuilder
from MovieRental_CanjuraHylton import movies
from MovieRental_CanjuraHylton import rentals
from MovieRental_CanjuraHylton import store
from datetime import datetime
from flask import render_template
from MovieRental_CanjuraHylton import app

comments = []
allMovies = []
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
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='We are a video rental store. We have several movies for you to enjoy.',
        comments = comments
        )
     
    comments.append(request.form["contents"])
    return redirect(url_for('about'))
    

@app.route('/login')
def login():
    """Renders the about page."""
    return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        message='Login to rent or return a movie.'
    )
    redirect(url_for('login'))

@app.route('/movies', methods = ['GET', 'POST'])
def movies():
    """Renders the movies page."""
    return render_template(
        'movies.html',
        title='Movies',
        year=datetime.now().year,
        message='Select from one of our many movies below:',
        allMovies = listBuilder.getAllMovieTitles,
    )     
    redirect(url_for('movies'))



@app.route('/rent')
def rent():
    """Renders the about page."""
    return render_template(
        'rent.html',
        title='Rent',
        year=datetime.now().year,
        message='Select a movie, the format and add it to your cart.'
    )

@app.route('/returns')
def returns():
    """Renders the about page."""
    return render_template(
        'returns.html',
        title='Return',
        year=datetime.now().year,
        message='Return outstanding movies.'
    )