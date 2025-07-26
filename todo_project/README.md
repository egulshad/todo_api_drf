# To-Do API (Django REST Framework)

This project is a RESTful API for managing a task list (ToDo list), developed using Django and Django REST Framework (DRF). It supports user registration, JWT-based authentication, task CRUD operations, filtering, pagination, and unit testing.

## Features

- Custom user model (username, password, first name, last name)
- JWT Authentication (register, login)
- Task management with CRUD operations
- Filter tasks by status
- Mark tasks as completed
- Pagination for task listing
- PostgreSQL database
- Unit tests for API endpoints

## Technologies Used

- Python 3.x
- Django 4.x
- Django REST Framework
- PostgreSQL
- Simple JWT

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/todo_project.git
cd todo_project

Create and activate a virtual environment:

python -m venv django_env
source django_env/bin/activate

Install dependencies:
pip install -r requirements.txt

Configure the database (PostgreSQL) in settings.py.

Run migrations:

python manage.py makemigrations
python manage.py migrate

Create a superuser:

python manage.py createsuperuser

Start the development server:

python manage.py runserver

API Endpoints
All endpoints require JWT token authentication. Use the token obtained from the /api/token/ endpoint in the Authorization header.

Authentication
POST /api/register/ - Register a new user

POST /api/token/ - Obtain JWT token

POST /api/token/refresh/ - Refresh JWT token


Task Endpoints

| Method | Endpoint                     | Description                |
| ------ | ---------------------------- | -------------------------- |
| GET    | /api/tasks/                  | List all tasks (paginated) |
| POST   | /api/tasks/                  | Create a new task          |
| GET    | /api/tasks/<id>/             | Retrieve a specific task   |
| PUT    | /api/tasks/<id>/             | Update a task (owner only) |
| DELETE | /api/tasks/<id>/             | Delete a task (owner only) |
| PATCH  | /api/tasks/<id>/complete/    | Mark task as completed     |
| GET    | /api/tasks/?status=Completed | Filter tasks by status     |

Pagination

Paginated results can be accessed with query parameters:

GET /api/tasks/?page=2

Running Tests

Make sure your virtual environment is active and database is migrated, then run:

python manage.py test todo_app

Project Structure

todo_project/
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── todo_app/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── tests.py
├── todo_project/
│   ├── settings.py
│   ├── urls.py
├── manage.py

Author
Developed by Gulshad Eyubova
