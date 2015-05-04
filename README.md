# Kiuss

This is an open sourse release of a representative site for Kiuss Collective built using Django framework.
You can freely use templates and styles or the entire code to make your own gallery sites.

## Using

### Requirements

You need to have these packages to be installed on your computer:

* python 2.7
* pip
* virtualenv

These packages are also required and could be installed with pip using [`requirements.txt`](requirements.txt) file:

* Django 1.5.12
* South 1.0
* Pillow 2.8.1
* easy-thumbnails 1.5

To do so, run

    [sudo] pip install -r requirements.txt

### Installation

To deploy this project on you machine just clone the repo:

    git clone https://github.com/chschtsch/kiuss.git

Then create your `local_settings.py` file in `kiuss` directory using `local_settings_example.py` example.

Also, read the docs for [Django 1.5](https://docs.djangoproject.com/en/1.5/), used in this project.

To set up your virtual environment, just run

    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

This will create `env` directory in project root and install all required packages locally.

For more information on usage read [virtualenv docs](https://virtualenv.pypa.io/en/stable/index.html).

### Running

You can always customize your site to run apache2, nginx or whatever you need. But here is how to make initial set up and a test run on development server.

First of all, set up database by running

    python manage.py syncdb

To use migrations with database read [South docs](http://south.readthedocs.org/en/latest/).

Uncomment these lines in `local_settings.py` file for debug mode:

    #DEBUG = True
    #TEMPLATE_DEBUG = DEBUG

For first run use built-in dev server:

    python manage.py runserver

Now you should have working app. Open `yoursitename.com/admin/` to add artworks and admin the site.

Also, you are welcome to fork this project!

## License

This project is licensed under [Mit License](MIT-LICENSE.txt).

[Fancybox](http://www.fancyapps.com/fancybox/) is licensed under [CC BY-NC 3.0](http://creativecommons.org/licenses/by-nc/3.0/).
