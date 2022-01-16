# DJANGO REST APIS
Django REST framework is a powerful and flexible toolkit for building Web APIs.
There are so many ways to develop apis in DRF but in our project we are using Generic Views.
We have implemented this concept on Profile Model.


Apart from that I have also covered the authentication part of DRF.
There are three types of authentication we can use in DRF:

1). BasicAuthentication Method 

2). SessionAuthentication Method

3). TokenAuthentication Method

# PREQUISITES

Following programmes should be installed on your computer to run this project properly:

Python 3.6+

Virtual Environment

To install virtual environment on your system use:

pip install virtualenv

# Installation and Running :

git clone https://github.com/Anuj2001/django-rest-apis/tree/master.git

virtualenv myenv

source venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

Open Browser and Type http://127.0.0.1:8000

# Supporting Materials:

Difference between Session Authentication And Token Authentication:
https://www.baeldung.com/cs/tokens-vs-sessions

For Video Tutorials:
https://www.youtube.com/results?search_query=django+rest+api+geeky+shows+

