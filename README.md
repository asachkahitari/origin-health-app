# Image Management App

This project is a full-stack solution for managing and categorizing a collection of images. The app includes user authentication and authorization, image upload and management, role-based access control (RBAC), lazy loading, pagination, error handling, and logging.

## Table of Contents

- [System Requirements](#system-requirements)
- [Getting Started](#getting-started)
- [System Design](#system-design)
- [Features](#features)

## System Requirements

- Python 3.x
- Django
- HTML, CSS, JavaScript for frontend

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/asachkahitari/origin-health-app.git

2. Navigate to the project directory:
    ```bash
    cd image_manager
    
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
5. Run migrations:
   ```bash
   python manage.py migrate
   
7. Start the Log Ingestor:
   ```bash
   python manage.py runserver


  The app will be available at http://localhost:8000/

## System Design

The system is designed to allow users to manage and categorize a collection of images securely. It includes user authentication and authorization, role-based access control (RBAC), image upload and management, lazy loading, pagination, error handling, and logging.

### System Architecture:

1. User Authentication and Authorization:

    Secure login page with authentication and authorization mechanisms.
    Support for two types of users: normal users and administrators.
    Different access levels for normal users and administrators.
  
2. Image Upload and Management:

    Admins can upload images to the system.
    Uploaded images are stored locally via the backend solution.

3. Role-Based Access Control (RBAC):

    Robust RBAC system with two roles: normal user and administrator.
    Different permissions for normal users and administrators.

4. Lazy Loading and Pagination:

    Lazy loading for images to optimize performance.
    Dynamic loading of images as the user scrolls through the page.
    Pagination to efficiently handle a large number of images.


## Features
    - User authentication and authorization.
    - Role-based access control (RBAC) with two roles: normal user and administrator.
    - Image upload and management.
    - Lazy loading and pagination for optimized performance.
    - Error handling and logging for graceful error management.
    - Dashboard pages for normal users and administrators.


##  How to Test

1. Run the Django development server:

    ```bash
    python manage.py runserver

2. Access the app:
    Open your web browser and go to http://localhost:8000/

3. Test user authentication:

    Register a new user or use existing credentials.
    Log in with the registered user or administrator credentials.

4. Test image upload:

    As an administrator, navigate to the admin dashboard.
    Upload new images and assign labels.

5. Test lazy loading and pagination:

    Scroll through the dashboard pages and observe the lazy loading of images.
    Test pagination to navigate through a large number of images.

6. Test error handling and logging:

    Intentionally trigger errors and observe the application's behavior.
    Check the logs for error details.

