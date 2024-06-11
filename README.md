# Django Diary Project

## Overview

The Django Diary Project is a web application built using the Django framework. It provides a secure way for users to create, edit, and delete diary entries. Users can log in with a username and password, and all diary entries are stored in an SQLite database. The project supports full CRUD (Create, Read, Update, Delete) operations for diary entries and includes user authentication and logout functionality.

## Features

- **User Authentication**: Secure login system using a username and password.
- **Create Diary Entry**: Users can create new diary entries with a title and content.
- **Edit Diary Entry**: Users can edit existing diary entries, updating the title and content.
- **Delete Diary Entry**: Users can delete diary entries.
- **View Diary Entries**: Users can view all their diary entries on a dashboard.
- **Logout**: Users can log out from the system.

## Technologies Used

- **Django**: The web framework used to build the application.
- **Python**: The programming language used for backend development.
- **HTML/CSS**: For creating the frontend interface.
- **SQLite**: The database used by Django for storing diary entries.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/diary-project.git
    cd diary-project
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv diary_env
    source diary_env/bin/activate  # On Windows use `diary_env\Scripts\activate`
    ```

3. **Install requirements**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

## Sample Images

### Login Page
![Login Page](https://github.com/PraveenGupta11001/Django-Diary-Project/assets/105053871/297d1c15-98a0-4a3d-b545-1fccc9f9842d)

### Dashboard with Diary Entries
![Dashboard](https://github.com/PraveenGupta11001/Django-Diary-Project/assets/105053871/9190a390-5d77-4830-a24c-79d6bd1aa53c)

### Create Diary Entry
![Create Diary Entry](https://github.com/PraveenGupta11001/Django-Diary-Project/assets/105053871/c6ebe601-c5d2-403c-8154-2f983c00efd4)
