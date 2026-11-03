import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# NEW TABLE: Tracks calendar appointments filled out by clients
cursor.execute('''
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_name TEXT NOT NULL,
        client_email TEXT NOT NULL,
        selected_date TEXT NOT NULL,
        selected_time TEXT NOT NULL,
        status TEXT DEFAULT 'Pending'
    )
''')

# Table 1: Main Client Passcode entries
cursor.execute('''
    CREATE TABLE IF NOT EXISTS client_galleries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_name TEXT NOT NULL,
        access_code TEXT UNIQUE NOT NULL
    )
''')

# Table 2: Image links for those galleries
cursor.execute('''
    CREATE TABLE IF NOT EXISTS gallery_images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        gallery_id INTEGER NOT NULL,
        image_filename TEXT NOT NULL,
        FOREIGN KEY (gallery_id) REFERENCES client_galleries (id) ON DELETE CASCADE
    )
''')

# Table 3: Homepage Carousel Images
cursor.execute('''
    CREATE TABLE IF NOT EXISTS homepage_carousel_images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        image_name TEXT NOT NULL
    )
''')

# Table 4: Testimonials and Images
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
