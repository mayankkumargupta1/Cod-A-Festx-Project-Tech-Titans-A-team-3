# Nirogi Janta

## Overview
Nirogi Janta is a web application designed to provide a comprehensive platform for managing health-related resources and information. Built with Django, this project focuses on promoting health awareness and providing easy access to health services.

## Features
- User-friendly interface for navigating health resources
- Admin panel for managing content
- Responsive design for accessibility on various devices

## Technologies Used
- Django
- Python
- HTML/CSS
- JavaScript
- SQLite/PostgreSQL

## Live Demo
Visit the live site at: [Nirogi Janta](http://your-live-site-link](https://cod-a-festx-project.onrender.com/)

## Local Installation

Follow these steps to set up the Nirogi Janta project locally:

### Prerequisites
Make sure you have the following installed on your machine:
- Python (version 3.x)
- pip (Python package installer)
- Git (for cloning the repository)

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/nirogi-janta.git
   cd nirogi-janta


Create a Virtual Environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the Required Packages:

bash
Copy code
pip install -r requirements.txt

Set Up the Database:

If using SQLite, the database will be created automatically.
If using PostgreSQL, make sure to create a database and update the DATABASES setting in settings.py accordingly.
Run Migrations:

bash
Copy code
python manage.py migrate
Create a Superuser (for accessing the admin panel):

bash
Copy code
python manage.py createsuperuser
Run the Development Server:

bash
Copy code
python manage.py runserver
