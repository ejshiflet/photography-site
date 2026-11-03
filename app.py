from flask import Flask, render_template
from flask_livereload import LiveReload
import sqlite3

app = Flask(__name__)
LiveReload(app)

@app.route('/')
def home():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    #For carousel
    cursor.execute("SELECT image_name FROM homepage_carousel_images")

    raw_images = cursor.fetchall()
    connection.close()

    carousel_images = [row[0] for row in raw_images]

    return render_template('home.html', carousel_images=carousel_images, testimonials=testimonial_creation())


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/wedding-investments')
def wedding_investments():
    return render_template('wedding_investments.html', testimonials=testimonial_creation())

@app.route('/lifestyle')
def lifestyle():
    return render_template('lifestyle.html', testimonials=testimonial_creation())

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

def testimonial_creation():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    
    cursor.execute("SELECT image_name, client_name, client_testimonial FROM testimonials")
    
    all_testimonials = cursor.fetchall()
    connection.close()
    
    testimonials = [row for row in all_testimonials]
    return testimonials

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
