
# Task Management Application

A simple task management application built with Django, designed to help users manage and track their tasks efficiently. This project includes a backend API using Django REST Framework to perform CRUD operations on tasks, with an admin interface to manage them.

## Features

- **Task Creation**: Create new tasks with a title, description, and due date.
- **Task Update**: Update task details including title, description, and status (completed or not).
- **Task Deletion**: Remove tasks when no longer needed.
- **Task Listing**: View all tasks in a list format through the API or Django admin interface.
- **Django Admin Interface**: Admin interface for managing tasks.
- **API Endpoints**: Built with Django REST Framework to allow interaction with tasks programmatically.

## Technologies Used

- **Backend**: Django
- **API Framework**: Django REST Framework
- **Database**: SQLite (default for Django, can be configured to use PostgreSQL or MySQL)
- **Admin Interface**: Django Admin
- **Python**: Python 3.x

## Project Structure

```
task_manager/
├── manage.py
├── task_manager/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── migrations/
└── db.sqlite3
```

## Getting Started

Follow the steps below to set up the project on your local machine:

### Prerequisites

- Python 3.x
- Django 5.1.x
- Django REST Framework
- SQLite (or other database options)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/salahsaeed19/task_manager.git
   cd task_manager
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations to set up the database:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser to access the Django admin interface:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the app in your browser:**
   Open your browser and go to `http://127.0.0.1:8000` to access the task management API. To access the Django admin interface, go to `http://127.0.0.1:8000/admin` and log in with the superuser credentials.

### API Endpoints

- `GET /api/tasks/`: List all tasks.
- `POST /api/tasks/`: Create a new task.
- `GET /api/tasks/{id}/`: Get details of a specific task.
- `PUT /api/tasks/{id}/`: Update an existing task.
- `DELETE /api/tasks/{id}/`: Delete a task.

## Contributing

Feel free to fork this repository, contribute improvements, and submit pull requests. All contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
