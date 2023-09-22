# Pfruit_Wed
Django-based web application for managing and displaying wedding photos. 
Users can browse through folders, view images, and download images if they are logged in.

## Installation: 

Install XAMPP server:

Create a database in localhost/phpmyadmin: 'pfruit_wm'

1. Clone the repository:

   ```bash
   git clone https://github.com/Devika1698/Pfruit_Wed.git

2. Create and activate a virtual environment(PyCharm): 
   virtualenv venv

3. Apply database migrations: 
   python manage.py migrate 

4. Load the data into the database:
   python manage.py loaddata data.json

5. Run the development server:
   python manage.py runserver

