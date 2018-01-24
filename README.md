# CSV API

This application is loading csv file content and give a RESTFULL API to access this content
# Installation

  - extract the zip file
  - csv file path is: `django-scv/mobile/file`
  - create virtual environment ` virtualenv venv`
  - activate the virtual envirtonment `soruce venv/bin/activate`
  - navigate to the project directory  `cd djanog-scv`
  - install requirements `pip install -r requirements.txt`
  - migrate the database `python manage.py makemigrations`
  - and after that run `python manage.py migrate`
  - run the application `python manage.py runserver 0.0.0.0:8000`

### Test Curl
  - To upload csv file content:
  ``` curl --request GET --url http://127.0.0.1:8000/api/upload ```
  - To Download csv file:
  ``` curl --request GET --url http://127.0.0.1:7000/api/exportcsv ```
  - To Read CSV file:
  ```curl --request GET --url http://127.0.0.1:7000/api/mobile/```
  - To Search in use : ```curl --request GET
  --url 'http://127.0.0.1:7000/api/search?q=item' ```