![HTML](https://img.shields.io/badge/html-F55600?style=for-the-badge&logo=HTML5&logoColor=white)
![CSS](https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=CSS3&logoColor=white)
![PYTHON](https://img.shields.io/badge/python-0000CC?style=for-the-badge&logo=Python&logoColor=white)


# Flare Judge
Flare is a centralized learning platform that pulls competitive programming resources from across the web and puts them all in one place. Flare has an array of resources including custom-curated tutorials, practice problems, and language-specific assistance to aid in the learning process for competitive programming for a wide range of skill levels.

## Running Locally For Development
Python 3.10+ is required
Node.js and npm are also required for tailwind CSS
you may use a global install or use a [virtual environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) (recommended)

Clone the project:
```bash
git clone https://github.com/storple/flare-judge
cd flare-judge
```

Then, install the required python dependencies:
```bash
python -m pip install -r requirements.txt
```
Create a ```.env.dev``` file in the root directory

Example .env.dev file:
```python
DEBUG=True
SECRET_KEY=KEY_HERE
DJANGO_ALLOWED_HOSTS=*
CSRF_TRUSTED_ORIGINS=
```

Install tailwind and its dependencies:
```bash
python manage.py tailwind install
```

Its also highly recommended that katex be installed through npm:
```bash
npm install katex

# or to not create a node_modules directory in the project
npm install -g katex
```

Then you can start the server:
```bash
python manage.py migrate

# the following two commands should be run in different terminals
python manage.py tailwind install
python manage.py runserver
```

to use the admin panel while in development, create a superuser account with the following: 
```bash
python manage.py createsuperuser
```
**NOTE:** In order to use this account to test all the website's functionality, manually create a profile for this account on the admin panel

## Admin Panel
Adding problems, lessons, and tags is very convenient thanks to the admin panel!

Go to the Django admin panel by entering the following link and log in

```
http://127.0.0.1:8000/admin_control/
```

Using the admin panel you can now easily add problems, lessons, and tags to the website!

![Django Admin Panel](/screenshots/django_admin_panel.png?raw=true)

