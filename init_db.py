import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()



cursor.execute('''
    CREATE TABLE IF NOT EXISTS portfolio_images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        image_filename TEXT NOT NULL,
        title TEXT,
        alt_text TEXT,
        category TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS homepage_carousel_images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        image_name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS testimonials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_name TEXT NOT NULL,
    client_name,
    client_testimonial TEXT NOT NULL
    )

''')




connection.commit()
connection.close()

print("Complete database blueprint generated successfully!")
