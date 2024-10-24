# Django Project Setup Guide

## TL;DR

1. Create a virtual environment in `.venv` for isolated dependencies.
2. Install dependencies from `requirements.txt`.
3. Generate migration files using `makemigrations`.
   ```bash
   python manage.py makemigrations
   ```
4. Apply migrations to update the database with `migrate`.
   ```bash
   python manage.py migrate
   ```
5. Start the development server with `runserver` to view the app locally.
   ```bash
   python manage.py runserver
   ```

## 1. Create a Virtual Environment (venv)

A **virtual environment** is an isolated Python environment that helps you manage dependencies separately for each project.

### Command to create the virtual environment:

- **On Unix/Linux/Mac:**
  ```bash
  python3 -m venv .venv
  ```
- **On Windows:**
  ```bash
  python -m venv .venv
  ```
  This creates a directory named .venv where the virtual environment is stored.

### Activate the virtual environment:

- **On Unix/Linux/Mac:**

  ```bash
  source .venv/bin/activate
  ```

- **On Windows:**
  ```bash
  python -m venv .venv
  ```
  Once activated, your terminal prompt will show .venv, indicating that the virtual environment is active.

## 2. Install Requirements

The requirements.txt file contains the necessary libraries and dependencies for your project. You can install them into your .venv environment by running:

```bash
pip install -r requirements.txt
```

This command ensures all required dependencies are installed within the virtual environment.

## 3. Run `python manage.py makemigrations`

Django uses a migration system to handle changes in the database structure. The `makemigrations` command looks at your models and creates migration files for any changes made.

```bash
python manage.py makemigrations
```

This generates migration files that describe the changes to be applied to the database, based on the models you’ve defined.

## 4. Run `python manage.py migrate`

To apply the changes defined in the migration files to your database, use the `migrate` command:

```bash
python manage.py migrate
```

This command creates or updates the database tables to match the structure defined by your models.

## 5. Run python `manage.py runserver`

To start Django’s development server and view your application, run the `runserver` command:

```bash
python manage.py runserver
```

By default, this runs the server locally at `http://127.0.0.1:8000/`. Open this URL in your browser to see your Django app.
