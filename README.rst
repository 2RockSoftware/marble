Requirements
------------

Below you will find basic setup and deployment instructions for the Marble
project. To begin you should have the following applications installed on your
local development system::

- Python >= 3.8
- Dev Tools (e.g. Ubuntu) `sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib` _
- `pipenv the latest`_
- Postgres >= 10
- git >= 1.7
- pipenv
- See also Pipfile

Project Setup
-------------

First clone the repository from BitBucket and switch to the new directory::

  $ git clone git@bitbucket.org:[ORGANIZATION]/marble.git
  $ cd marble

Next, create a virtual environment and install all of the requirements::

  (marble)$ pipenv shell --python 3.8
  (marble)$ pipenv install --dev

Now, create a local settings file and set your DJANGO_SETTINGS_MODULE to use it:::

  cp marble/settings/local.example.py marble/settings/local.py
  echo "DJANGO_SETTINGS_MODULE=marble.settings.local" > .env

Exit the virtualenv and reactivate it to activate the settings just changed::

  deactivate
  pipenv shell

Create the Postgres database and run the initial syncdb/migrate::

  createdb -E UTF-8 marble
  python manage.py migrate

You should now be able to run the development server::

  python manage.py runserver

Compile front-end 

  npm install 
  npm run dev 


Wagtail
-------

Create a superuser 

  python manage.py createsuperuser 

Log into the Wagtail admin and set up a site 

  http://localhost:8000/admin/wagtail 


Testing
--------

Run the following command to run the test suite::

    python manage.py test


Code Quality
--------------
We use auto formatter to ensure the quality of the code. New developers need to ensure to run the following commands
to setup auto-formatting::

    pipenv install
    pipenv install --dev
    pre-commit install

You could also manually run the pre-commit checks like this::

    pre-commit run --all-files

Dokku Deployment
----------------

Staging deployment::

    git push staging {local_branch}:develop

Production deployment::

    git push production {local_branch}:master

We use the buildpacks in .buildpacks

Postgres (Ubuntu)
--------

Requirements

1.  Install postgres (see previous notes)
2.  User is in sudoer file


Find your user name

```
$ whoami
userabc
```

Login to postgres as super user

```
$ sudo -u postgres psql
postgres=# \du
                                  List of roles
 Role name |                         Attributes                         | Member of
-----------+------------------------------------------------------------+-----------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 userabc   |                                                            | {}

```

Add Super User role to userabc
```
postgres=# ALTER USER userabc WITH SUPERUSER;
ALTER ROLE
```



Front End
--------

- `nvm use 16`
- `npm install`
- `npm run build` or `npm run dev`
