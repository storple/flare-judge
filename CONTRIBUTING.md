## Local Development
Python 3.10+ is required
Node.js and npm are also required for tailwind CSS

You may use a global install or use a [virtual environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) (recommended)

Clone the project:
```bash
git clone https://github.com/storple/flare-judge
cd flare-judge
```
Create a ```.env.dev``` file in the root directory (i.e. ```flare-judge/.env.dev```)

Example .env.dev file:
```python
DEBUG=True
SECRET_KEY=KEY_HERE
DJANGO_ALLOWED_HOSTS=*
CSRF_TRUSTED_ORIGINS=
```

Then, install the required python dependencies:
```bash
cd app
python -m pip install -r requirements.txt
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
# if the following fails, create a folder called db
python manage.py migrate

# the following two commands should be run in different terminals
python manage.py tailwind start
python manage.py runserver
```

to use the admin panel while in development, create a superuser account with the following: 
```bash
python manage.py createsuperuser
```
**NOTE:** In order to use this account to test all the website's functionality, manually create a profile for this account on the admin panel
