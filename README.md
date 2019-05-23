# project_for_getdev
This is a getdev project test

**Atleast Python 3.6 is required**

**Technology Used:** Django 2.0.6 (Python 3)

**Database:** SQLite 3 (SQLite is used because it can be safely assumed that it would not be a very busy site and enterprise level database can be avoided)


## Installation

- Clone repository

    ```bash
    git clone https://github.com/Akoh1/project_for_getdev.git
    ```

- Setup virtualenvironment with virtualenvwrapper

    ```bash
    mkvirtualenv getdev
    ```

- Install requirements

    ```bash
    pip install -r requirements.txt

- Migrate
    ```bash
    python manage.py migrate
    ```
- Run Server
    ```bash
    python manage.py runserver
    ```    