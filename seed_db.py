import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

#============================homepage carousel seeding=============================
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

#=========================== testimonial seeding===================================

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


#===================================portfolio image seeding==========================

portfolio_mocks = [
    ('MalPortraits(39of88).jpg', 'Portraits'),
    ('DSC05239.jpg', 'Wedding'),
    ('Havi(185of185).jpg', 'Portraits'),
    ('MalGraduation(75of262).jpg', 'Graduation'),
    ('JordanFamilyMini(1of38).jpg', 'Family'),
    ('Mel(18of83).jpg', 'Portraits'),
    ('NicoleandPatrick(29of39).jpg', 'Wedding'),
    ('DSC02128.jpg', 'Graduation'),
    ('SabaGraduation(4of40).jpg', 'Portraits'),
    ('JordanFamilyMini(8of38).jpg', 'Family'),
    ('MalGraduation(13of262).jpg', 'Graduation'),
    ('Havi(125of185).jpg', 'Portraits'),
    ('DSC05173.jpg', 'Wedding'),
    ('SabaGraduation(18of40).jpg', 'Graduation'),
    ('MalPortraits(54of88).jpg', 'Portraits'),
    ('DSC04934.jpg', 'Wedding'),
    ('MalGraduation(7of262)-sRGB,Perceptual.jpg', 'Graduation'),
    ('Mel(10of83).jpg', 'Portraits'),
    ('JordanFamilyMini(21of38).jpg', 'Family'),
    ('DSC02266.jpg', 'Graduation'),
    ('MalPortraits(65of88).jpg', 'Portraits'),
    ('DSC05045.jpg', 'Wedding'),
    ('MalGraduation(91of262).jpg', 'Graduation'),
    ('LillySeniorPhotos(9of58).jpg', 'Portraits'),
]

# Only insert rows that have a real category
ready = [(name, cat) for name, cat in portfolio_mocks if cat != 'TODO']
todo_files = [name for name, cat in portfolio_mocks if cat == 'TODO']

cursor.execute("DELETE FROM portfolio_images")
cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'portfolio_images'")
cursor.executemany(
    'INSERT INTO portfolio_images (image_filename, title, alt_text, category) VALUES (?, ?, ?, ?)',
    [(name, None, f'{cat} photography by Shiflet Studios', cat) for name, cat in ready]
)

if todo_files:
    print(f"Skipped {len(todo_files)} images still marked TODO:")
    for name in todo_files:
        print("  ", name)



#=====================================================================================


connection.commit()
connection.close()


print("Database updates successful!")
