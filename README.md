# 🎓 Student Database Management System

A lightweight and efficient web application built with Django to manage student records. This project uses Django's default SQLite database and is designed to run locally on your machine.

---

## 🚀 Features

* **Create:** Add new student profiles to the database.
* **Read:** View a complete list of all enrolled students and their details.
* **Update:** Edit existing student information easily.
* **Delete:** Remove student records from the system.
* **Admin Panel:** Built-in Django admin interface for easy database management.

---

## 🛠️ Tech Stack

* **Backend Framework:** Django (Python)
* **Database:** SQLite3 (Default, Local)
* **Frontend:** HTML, CSS (Include Bootstrap/Tailwind if you used it)

---

## ⚙️ Local Setup & Installation

Follow these steps to get the project running on your local machine (`localhost`). No external database setup is required!

### 1. Prerequisites
Ensure you have Python installed on your system. You can check by running:
```bash
python --version
```
### 2. Install Django
If you haven't already installed Django, you can do so using pip:

```bash
pip install django
```
(Note: It is highly recommended to do this inside a virtual environment).

### 3. Apply Database Migrations
Navigate to the project folder (where the manage.py file is located) and set up the SQLite database tables:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create a Superuser (Optional but Recommended)
To access the Django Admin panel, create an admin account:
```bash
python manage.py createsuperuser
```

### 5. Run the Local Development Server
Start the server to view the application:
```bash
python manage.py runserver
```

---


# 🌐 Usage


- Once the server is running, open your web browser and navigate to: 👉 http://127.0.0.1:8000/ (or http://localhost:8000/)
- To access the admin dashboard, go to: 👉 http://127.0.0.1:8000/admin/

  ---
  

#🗄️ Database Note


- This project uses SQLite, which stores the entire database in a single local file (db.sqlite3) inside the project directory. You do not need to install MongoDB, MySQL, or Postgres to run this application.

---


### 👩‍💻 Author


**Laxmi Parmanandani** 
- LinkedIn: https://www.linkedin.com/in/laxmi-parmanandani-63733a386/
