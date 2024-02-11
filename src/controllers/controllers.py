from flask import render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3, re

def homepage():
    return render_template('index.html')

# Signup route

def get_rooms():
    conn = sqlite3.connect('databases/students-data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, room_name FROM rooms")
    rooms = cursor.fetchall()
    conn.close()

    return rooms

def validate_username(username):
    if not (3 <= len(username) <= 20):
        return False

    pattern = re.compile("^[a-zA-Z0-9_-]+$")
    return bool(pattern.match(username))

def signup_page():
    if request.method == 'POST':
        username = request.form['username']
        raw_user_password = request.form['password']
        room_id = request.form['room-id']

        if not validate_username(username):
            return "Invalid nickname"

        hashed_user_password = generate_password_hash(raw_user_password)

        conn = sqlite3.connect('databases/students-data.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, password, room_id) VALUES (?, ?, ?)", (username, hashed_user_password, room_id))
        conn.commit()
        conn.close()

        return redirect('/')

    rooms = get_rooms()
    return render_template('signup.html', rooms=rooms)

# Login route

def login_page():
    if request.method == 'POST':
        inserted_username = request.form['username']
        inserted_user_password = request.form['password']

        if not  validate_username(inserted_username):
            return "Invalidad username"

        conn = sqlite3.connect('databases/students-data.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM students WHERE name = ?", (inserted_username,))
        stored_password = cursor.fetchone()

        if stored_password:
            if check_password_hash(stored_password[0], inserted_user_password):
                return redirect('/')

        return "Login failed"

    return render_template('login.html')