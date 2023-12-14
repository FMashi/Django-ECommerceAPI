# Django E-CommerceAPI

This repository contains the source code for a RESTful API built using Django and the Django REST Framework (DRF). The project focuses on demonstrating the implementation of essential concepts such as Django setup, model serialization, authentication, routers, and the use of generic or model viewsets. The goal is to provide a comprehensive example that adheres to best practices in API development, offering a fully functional API system.

## Project Structure

The project adopts a well-organized structure to enhance clarity and maintainability. Key components are situated within the 'app' folder, including settings and the core functionality of the Django E-Commerce API.

### Example Directory Structure

```
Django-ECommerceAPI/
        ├── api
        │   ├── __init__.py
        │   ├── admin.py
        │   ├── apps.py
        │   ├── migrations
        │   │   └── __init__.py
        │   ├── models.py
        │   ├── serializers.py
        │   ├── tests.py
        │   ├── urls.py
        │   └── views.py
        ├── app
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        ├── manage.py
        └── requirements.txt
```

## Setting Up Virtual Environment and Installing Requirements

To run this project locally, follow these steps to set up a virtual environment and install the required dependencies.

### 1. Create a Virtual Environment

Create a virtual environment, and navigate to the 'app' folder and using the following commands:

```bash
python -m venv venv
cd app
```

### 2. Activate the Virtual Environment

On Windows, activate the virtual environment with:

```bash
venv\Scripts\activate
```

On Unix or MacOS, activate the virtual environment with:

```bash
source venv/bin/activate
```

### 3. Install Requirements

With the virtual environment activated, install the project dependencies from the 'requirements.txt' file:

```bash
pip install -r requirements.txt
```

## Running the Django E-Commerce API

After setting up the virtual environment and installing the requirements, you can run the API locally using the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

This will apply migrations and start the development server. You can access the API at `http://localhost:8000/`.
