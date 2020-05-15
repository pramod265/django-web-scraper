**Web scraper Project**

This project is using Django with python3.

This project is for scraping data from sitemaps of websites.co.in with set threshold.
We can also scrape data from any other url if we want.
---

## Initial setup

You will have to follow below steps if you are using virtual envirnoment.

1. Create virtual using python3 by below command.

		virtualenv -p python3 envname

2. Switch to your environment by.

		source path-to-env/bin/activate

3. Clone your project by.

        git clone https://github.com/pramod265/web_scraper.git

---

## Project Setup

Django project setup.

1. Move into your project path.

		cd /path/to/your/project/

2. Install the requirments of project.

		pip install -r requirements.txt

3. Edit your settings files.

		settings.py
		// you can create your own settings file base on that update __init__.py

		DATABASES = {
		    'default': {
		        'ENGINE': 'django.db.backends.postgresql_psycopg2',
		        'NAME': '', //databse name
		        'USER': '',  //Postgres user
		        'PASSWORD': '', //postgres password
		        'HOST': '127.0.0.1',
		        'PORT': '5432',
		    },
		}

    Note - We are using postgres for DATABASE.  if you want to use sqlite3  you can use that and change you DATABASES key accordingly.


4. Create your database migrations by.

		python manage.py makemigrations

5. Make your database by below command.

		python manage.py migrate

6. Run your project by.

		python manage.py runserver

Solve your requirements as per the error if generated at time of project setup.

---

## Your project Usage.

1. Create your super user for django admin.

		python manage.py createsuperuser

2. Access your admin in browser by.

		http://YourUrl/admin/

3. Access your api in browser by.

		http://YourUrl/api/

---

POST /api/scrape/ with Threshold [default will be 10]

    http://0.0.0.0:8000/api/scrape/

    Headers
        Content-Type    application/json

    Body (application/json)
        {
            "threshold":8
        }

POST /api/scrape/ with URL

    http://0.0.0.0:8000/api/scrape/

    Headers
        Content-Type     application/json

    Body (application/json)
    {
        "url":"https://docs.djangoproject.com/en/3.0/"
    }

---
