# Easy Blog Django

Easy Blog Django is a simple blog project by [@giantryansaul].

  - Simple home page layout that displays latest blog entries, date and author
  - Tag support for organizing posts into categories
  - User registration (but no ability to create comments yet)
  - Highlight code blocks
  - Highly customizable

Huge thanks to [@audreyr] and [@pydanny] for the book [Two Scoops of Django] and their [cookiecutter] tool that greatly helped shape the design of this project.

### Planned Features and To-dos

I intend to add features as they are needed on my own blogs or by popular request.

  - User comments on posts
  - Sample dataset for new blogs
  - Heroku deployment
  - EC2 deployment
  - Docker deployment
  - Unit tests (I know, I know, I should have created them before anything else, but this is my first project, so please be kind).

### Version

0.1.0

### Tech used

Easy Blog uses many open source technolgies to run:

* [Django] - Web framework built in Python.
* [cookiecutter] - Django project tool that installs many necessary libraries. I thought it was worth mentioning again that this tool is amazing for kick-starting new projects.
* [Bootstrap] - Used for front-end design and layout.
* [Clean Blog] - Bootstrap template used for this blog.
* [crispy-forms] - Django forms tool that automatically creates great-looking Bootstrap forms.
* [ckeditor] - Rich text editor used on forms with code snippet support.
* [django_wysiwyg] - Used to implement the above Rich Text Editor.

### Setup

Clone this repository locally and create a new database. This project was originally created using Postgres, but you are welcome to use MySQL or any other Django-supported database.

Go to `config/settings/local.py` and find the `DATABASES` setting, change your database properties accordingly:
```
DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    # Example: postgres://db_owner:password@dbserver_ip:port/db_name
    'default': env.db("DATABASE_URL", default="postgres://easyuser:password@localhost/easy_blog_django"),
}
```

Within your `bash_profile.sh` add a new secret key for Django, replace `my_easy_blog_key` with any random key string:
```
export EASY_BLOG_KEY=my_easy_blog_key
```
Run the migrate script to have Django create your database schema:
```
python manage.py migrate
```
Finally start the server:
```
python manage.py runserver
```
If everything worked you should be able to get to your new blog in your browser by going to `localhost:8000`

### Development

Please contribute! Django makes it super easy to update code.

Easy Blog Django is written with Class Based Views (CBV) and I attempted to stick to this very strictly, so any submissions that use Function Based Views may be rejected.

License
----
The MIT License (MIT)

Copyright (c) 2015 Ryan Saul

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

   [@giantryansaul]: <https://github.com/giantryansaul>
   [Django]: <https://www.djangoproject.com/>
   [Clean Blog]: <http://startbootstrap.com/template-overviews/clean-blog/>
   [ckeditor]: <http://ckeditor.com/>
   [Bootstrap]: <http://getbootstrap.com/>
   [Two Scoops of Django]: <http://twoscoopspress.org/products/two-scoops-of-django-1-8>
   [cookiecutter]: <https://github.com/audreyr/cookiecutter>
   [@audreyr]: <https://github.com/audreyr>
   [@pydanny]: <https://github.com/pydanny>
   [crispy-forms]: <http://django-crispy-forms.readthedocs.org/>
   [django_wysiwyg]: <https://github.com/pydanny/django-wysiwyg>

