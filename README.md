![HTML](https://img.shields.io/badge/html-F55600?style=for-the-badge&logo=HTML5&logoColor=white)
![CSS](https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=CSS3&logoColor=white)
![PYTHON](https://img.shields.io/badge/python-0000CC?style=for-the-badge&logo=Python&logoColor=white)


# Flare Judge
A centralized learning platform that pulls competitive programming resources from across the web and puts them all in one place. Flare has an array of resources including custom-curated tutorials, practice problems, and language-specific assistance to aid in the learning process for competitive programming for a wide range of skill levels.

## Run Locally
Python 3.10+ required
you may use the global install or use a [virtual environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) (recommended)

Clone the project
```bash
git clone https://github.com/storple/flare-judge
cd flare-judge
```

Install dependencies
```bash
python -m pip install -r requirements.txt
```
To run this project, you will need to add the following environment variables to your .env file

Example:
```python
SECRET_KEY = "KEY HERE"
DEBUG = False
```

Start the server

```bash
python manage.py migrate
python manage.py runserver
```

## Admin Panel
Adding problems, lessons, and tags is very convenient thanks to the admin panel!

To use the admin panel, first create a superuser:

```bash
python manage.py createsuperuser
```

Go to the Django admin panel by entering the following link and log in

```
http://127.0.0.1:8000/admin/
```

Using the admin panel you can now easily add problems, lessons, and tags to the website!

![Django Admin Panel](https://github.com/storple/flare-judge/blob/main/screenshots/django_admin_panel.png?raw=true)

