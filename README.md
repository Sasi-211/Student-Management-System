# Student Management System

Student Management System

A web-based Student Management System developed using Django that helps manage student records efficiently. This application allows users to add, view, update, and delete student information through a simple and user-friendly interface.

Features

- Add new students
- View all student records
- Change student details
- Search for students
- User-friendly interface
- Database integration using SQLite

Technologies Used

- Python
- Django
- HTML
- SQLite

Project Structure

StudentManagementSystem/
│
├── manage.py

├── starting/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│

├── starting_app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
└── db.sqlite3

Installation

1. Clone the repository:

git clone <repository-url>

2. Navigate to the project directory:

cd StudentManagementSystem

3. Install dependencies:

pip install -r requirements.txt

4. Apply migrations:

python manage.py migrate

5. Run the development server:

python manage.py runserver

6. Open your browser and visit:

http://127.0.0.1:8000/admin

7. If u want to view one by one student details
 
http://127.0.0.1:8000/api/student/1

Usage

- Add student details through the form.
- View all students in the student list.
- Edit student information when required.
- Delete records that are no longer needed.

Future Enhancements

- Student attendance management
- Marks and grade tracking
- Authentication and authorization
- Export student data to Excel/PDF
- Dashboard with statistics

Author

Developed by Sasi🤓.
