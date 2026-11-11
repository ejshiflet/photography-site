from flask import Flask, request, redirect, render_template, url_for
import sqlite3
import os, smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/')
def home():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    #For carousel
    cursor.execute("SELECT image_name FROM homepage_carousel_images")

    raw_images = cursor.fetchall()
    connection.close()

    carousel_images = [row[0] for row in raw_images]

    return render_template('home.html', page_class='home-page', carousel_images=carousel_images, testimonials=testimonial_creation())


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', page_class='portfolio-page')

@app.route('/wedding-investments')
def wedding_investments():
    return render_template('wedding_investments.html', page_class='wedding-investments-page', testimonials=testimonial_creation())

@app.route('/lifestyle')
def lifestyle():
    return render_template('lifestyle.html', page_class='services-page', testimonials=testimonial_creation())

@app.route('/about')
def about():
    return render_template('about.html', page_class='about-page')

@app.route('/faq')
def faq():
    return render_template('faq.html', page_class='faq-page')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        if request.form.get('website'):   # honeypot: bots fill this in
            return redirect(url_for('contact'))

        first = request.form['first-name']
        last = request.form['last-name']
        email = request.form['email']
        message = request.form['message']

        msg = EmailMessage()
        msg['Subject'] = f'[Shiflet Studios] New message from {first} {last}'
        msg['From'] = os.environ['GMAIL_USER']
        msg['To'] = os.environ['GMAIL_USER']
        msg['Reply-To'] = email
        msg.set_content(f'From: {first} {last} <{email}>\n\n{message}')

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(os.environ['GMAIL_USER'], os.environ['GMAIL_APP_PASSWORD'])
                server.send_message(msg)
        except Exception as e:
            print('Email error:', e)
            return redirect(url_for('contact', error=1))

        return redirect(url_for('contact', sent=1))

    return render_template('contact.html', page_class='contact-page')

def testimonial_creation():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    
    cursor.execute("SELECT image_name, client_name, client_testimonial FROM testimonials")
    
    all_testimonials = cursor.fetchall()
    connection.close()
    
    testimonials = [row for row in all_testimonials]
    return testimonials

if __name__ == '__main__':
    from flask_livereload import LiveReload
    LiveReload(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
