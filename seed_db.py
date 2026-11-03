import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# 1. Insert mock homepage carousel images
# Make sure you actually have photos named sample1.jpg, etc. inside your static/photos/ folder!
homepage_mocks = [('photo1.png',), ('photo2.png',), ('photo3.png',), ('sample1.jpg',), ('sample2.jpg',), ('sample3.jpg',), ('service1.png',)]

cursor.execute("DELETE FROM homepage_carousel_images")
cursor.executemany('INSERT INTO homepage_carousel_images (image_name) VALUES (?)', homepage_mocks)


testimonial_mocks = [
    (
        'photo2.png',
        'Evan',
        'I cannot thank him enough for making my vision, idea, and wishes a reality. The conversation and the smooth process is what sets him apart'
    ), 
    (
        'service1.png',
        'Mal',
        'I cannot thank him enough for making my vision, idea, and wishes a reality. The conversation and the smooth process is what sets him apart'
    ),
    (
        'service3.png',
        'Stevens Family',
        'I cannot thank him enough for making my vision, idea, and wishes a reality. The conversation and the smooth process is what sets him apart'
    )
    ]

cursor.execute("DELETE FROM testimonials")
cursor.executemany('INSERT INTO testimonials (image_name, client_name, client_testimonial) VALUES (?, ?, ?)', testimonial_mocks)

connection.commit()
connection.close()


print("Database updates successful!")
