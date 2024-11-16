
# Task Management Application

A task management application built with Django, enhanced with a range of features for efficient tracking and handling of tasks. This project includes a backend API using Django REST Framework, allowing users to perform CRUD operations on tasks with features like user assignments, priority settings, and due date reminders.

## Features

- **Task Creation**: Create new tasks with a title, description, and due date.
- **Task Update**: Update task details, including title, description, and status (completed or not).
- **Task Deletion**: Remove tasks when no longer needed.
- **Task Listing**: View all tasks in a list format through the API or Django admin interface.
- **Task Comments**: Add, view, and manage comments on each task, with user attribution for each comment.
- **Django Admin Interface**: Admin interface for managing tasks and comments.
- **API Endpoints**: Built with Django REST Framework for interacting with tasks and comments programmatically.
- **Task Filtering and Sorting**:
  - Filter tasks by priority, completion status, or category.
  - Sort tasks by priority, due date, or title.

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

- **Tasks**
  - `GET /api/tasks/`: List all tasks.
  - `POST /api/tasks/`: Create a new task.
  - `GET /api/tasks/{id}/`: Get details of a specific task.
  - `PUT /api/tasks/{id}/`: Update an existing task.
  - `DELETE /api/tasks/{id}/`: Delete a task.

- **Comments**
  - `GET /api/comments/`: List all comments.
  - `POST /api/comments/`: Create a new comment for a task.
  - `GET /api/comments/{id}/`: Get details of a specific comment.
  - `PUT /api/comments/{id}/`: Update an existing comment.
  - `DELETE /api/comments/{id}/`: Delete a comment.

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/salahsaeed19/task-manager?tab=MIT-1-ov-file) file for details.
