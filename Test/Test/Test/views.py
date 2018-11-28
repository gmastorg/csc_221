"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Test import app

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
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/login')
def login():
    """Renders the about page."""
    return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/movies')
def movies():
    """Renders the about page."""
    return render_template(
        'movies.html',
        title='Movies',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/rent')
def rent():
    """Renders the about page."""
    return render_template(
        'movies.html',
        title='Rent',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/returns')
def returns():
    """Renders the about page."""
    return render_template(
        'returns.html',
        title='Return',
        year=datetime.now().year,
        message='Your application description page.'
    )