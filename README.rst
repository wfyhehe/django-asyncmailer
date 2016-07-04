Django AsyncMailer
============

Async email solution w/ multiple SMTP credentials, load-balancing and blacklist.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-asyncmailer

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/andyfangdz/django-asyncmailer.git#egg=asyncmailer

TODO: Describe further installation steps (edit / remove the examples below):

Add ``asyncmailer`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'asyncmailer',
    )

Add the ``asyncmailer`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = [
        url(r'^asyncmailer/', include('asyncmailer.urls')),
    ]

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load asyncmailer_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate asyncmailer


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-asyncmailer
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch

In order to run the tests, simply execute ``tox``. This will install two new
environments (for Django 1.8 and Django 1.9) and run the tests against both
environments.