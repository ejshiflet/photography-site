import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# 1. Insert mock homepage carousel images
# Make sure you actually have photos named sample1.jpg, etc. inside your static/photos/ folder!
homepage_mocks = [
    ('MalPortraits(39of88).jpg',),
    ('Mel(18of83).jpg',),
    ('DSC05239.jpg',),
    ('Havi(185of185).jpg',),
    ('MalGraduation(75of262).jpg',),
    ('DSC02128.jpg',),
    ('JordanFamilyMini(1of38).jpg',),
    ('SabaGraduation(4of40).jpg',),
    ('MalPortraits(54of88).jpg',),
    ('Mel(10of83).jpg',),
    ('DSC05173.jpg',),
    ('Havi(125of185).jpg',),
    ('MalGraduation(13of262).jpg',),
    ('LillySeniorPhotos(9of58).jpg',),
    ('JordanFamilyMini(8of38).jpg',),
    ('MalPortraits(65of88).jpg',),
    ('DSC04934.jpg',),
    ('MalGraduation(7of262)-sRGB,Perceptual.jpg',),
    ('DSC05045.jpg',),
    ('MalGraduation(91of262).jpg',),
    ('DSC02266.jpg',),
    ('JordanFamilyMini(21of38).jpg',),
    ('SabaGraduation(18of40).jpg',),
]


cursor.execute("DELETE FROM homepage_carousel_images")
cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'homepage_carousel_images'")
cursor.executemany('INSERT INTO homepage_carousel_images (image_name) VALUES (?)', homepage_mocks)


testimonial_mocks = [
    (
        'Mel(12of83).jpg',
        'Sirgut',
        'I cannot thank him enough for making my vision, idea, and wishes a reality. The conversation and the smooth process is what sets him apart'
    ), 
    (
        'MalGraduation(7of262)-sRGB,Perceptual.jpg',
        'Mal',
        'I cannot thank him enough for making my vision, idea, and wishes a reality. The conversation and the smooth process is what sets him apart'
    ),
    (
        'JordanFamilyMini(21of38).jpg',
        'Jordan Family',
        'I cannot thank him enough for making my vision, idea, and wishes a reality. The conversation and the smooth process is what sets him apart'
    )
    ]

cursor.execute("DELETE FROM testimonials")
cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'testimonials'")
cursor.executemany('INSERT INTO testimonials (image_name, client_name, client_testimonial) VALUES (?, ?, ?)', testimonial_mocks)

connection.commit()
connection.close()


print("Database updates successful!")
