![HTML](https://img.shields.io/badge/html-F55600?style=for-the-badge&logo=HTML5&logoColor=white)
![CSS](https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=CSS3&logoColor=white)
![PYTHON](https://img.shields.io/badge/python-0000CC?style=for-the-badge&logo=Python&logoColor=white)


# Flare Judge
A competitive programming roadmap for aspiring high school students who want to succeed.
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
