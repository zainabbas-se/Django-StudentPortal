# Student Portal

## Overview

The Student Portal is a Django-based web application for managing student information and performing administrative tasks. It features user registration, login, and CRUD (Create, Read, Update, Delete) operations. Built with Django, it incorporates best practices for web development and security.

## Features

- **User Registration:** Allows students to create accounts.
- **User Login:** Secure login for registered users.
- **CRUD Operations:** Manage student records (add, edit, delete).
- **Authorization:** Access control based on user roles.

## Technologies Used

- **Django:** Web framework.
- **Python:** Programming language.
- **Bootstrap 4.5.2:** Styling and responsive design.
- **SQLite:** Database management.
- **HTML/CSS:** Front-end development.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/StudentPortal-CRUD.git
    cd StudentPortal-CRUD
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

6. Create a superuser (admin):
    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```bash
    python manage.py runserver
    ```

8. Access the application:

    Open `http://127.0.0.1:8000/` in your browser.

## Usage

- **Registration:** Navigate to the registration page to create an account.
- **Login:** Use the login page to access the portal.
- **CRUD Operations:** Use the student management interface for CRUD operations.

## Contributing

I want you to know that contributions are welcome. Please:

1. Fork the repository.
2. Create a new branch.
3. Make changes.
4. Commit changes.
5. Push to your fork.
6. Create a pull request.

<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
