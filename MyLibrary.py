import sqlite3

conn = sqlite3.connect('MyLibrary.db')
cursor = conn.cursor()
cursor.execute('''
 CREATE TABLE IF NOT EXISTS books(
    title TEXT,
    author TEXT,
    genre TEXT CHECK(genre IN ('Male', 'Female')),
    year TEXT,
    status TEXT CHECK(status IN ('Read', 'Not-Read'))
 )
''')
while True:
    print("\nChoice:\n    1-Add [A]\n    2-Edit_Status [E]\n    3-Exit [X]\n")
    choice = input("Choice: ").strip().upper()
    if choice == 'A':
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        while True:
            genre = input("Enter book genre (Male/Female): ").strip().capitalize()
            if genre in ('Male', 'Female'):
                break
            print("Invalid genre. Please enter either 'Male' or 'Female'.")
        year = input("Enter book year: ")
        while True:
            status = input("Enter book status (Read/Not-Read): ").strip().capitalize()
            if status in ('Read', 'Not-Read'):
                break
            print("Invalid status. Please enter either 'Read' or 'Not-Read'.")
        cursor.execute("INSERT INTO books (title, author, genre, year, status) VALUES (?, ?, ?, ?, ?)", (title, author, genre, year, status))
        conn.commit()
        print("\nThe book was added successfully!\n")
    elif choice == 'E':  
        while True:
            status = input("Enter new status (Read/Not-Read): ").strip().capitalize()
            if status in ('Read', 'Not-Read'):
                break
            print("Invalid status. Please enter either 'Read' or 'Not-Read'.")
        title = input("Enter book title to update: ")
        cursor.execute('''
         UPDATE books  
         SET status = ?  
         WHERE title = ?  
        ''', (status, title))
        conn.commit()
        print("\nThe status was updated successfully!\n")
    elif choice == 'X':
        print("\nExiting program...\n")
        break
    else:
        print("\nInvalid choice. Please enter A, E, or X.\n")
conn.close()
