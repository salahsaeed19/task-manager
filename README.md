
# Task Management Application

A task management application built with Django, enhanced with a range of features for efficient tracking and handling of tasks. This project includes a backend API using Django REST Framework, allowing users to perform CRUD operations on tasks with features like user assignments, priority settings, and due date reminders.

## Features

- **Task Creation**: Users can create tasks with a title, description, priority level, and due date.
- **Task Assignment**: Tasks can be assigned to specific users.
- **Status Management**: Update the status of tasks, such as marking them as "In Progress" or "Completed".
- **Priority Levels**: Set different priority levels to manage task urgency.
- **Due Date Reminders**: Configure reminders for due dates to help users stay on track.
- **Task Filtering**: Filter tasks by status, priority, or assigned user.
- **API Endpoints**: Django REST Framework provides easy interaction with tasks programmatically.

## Technologies Used

- **Backend**: Django 5.1.3
- **API Framework**: Django REST Framework
- **Database**: SQLite (configurable to PostgreSQL or MySQL)
- **Admin Interface**: Django Admin
- **Python Version**: Python 3.12.6

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
├── db.sqlite3
├── venv
├── manage.py
├── README.md
```

## Getting Started

Follow these steps to set up the project on your local machine:

### Prerequisites

- Python 3.12.6
- Django 5.1.3
- Django REST Framework
- SQLite (or an alternative database)

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
     venv\Scriptsctivate
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
   Open your browser and go to `http://127.0.0.1:8000` to access the task management API. For the Django admin interface, go to `http://127.0.0.1:8000/admin` and log in with the superuser credentials.

### API Endpoints

- `GET /api/tasks/`: List all tasks.
- `POST /api/tasks/`: Create a new task.
- `GET /api/tasks/{id}/`: Get details of a specific task.
- `PUT /api/tasks/{id}/`: Update an existing task.
- `DELETE /api/tasks/{id}/`: Delete a task.

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/salahsaeed19/task-manager?tab=MIT-1-ov-file) file for details.
