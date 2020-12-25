# blog-app-in-union
Building A Blog App In Union using Django 2.2.1
https://github.com/ingafter60/blog-app-in-union

### 1. Initial commit - Create github repository

### 2. Create 'venv39221' and Django project 'core'

        modified:   .gitignore
        modified:   README.md
        new file:   core/__init__.py
        new file:   core/settings.py
        new file:   core/urls.py
        new file:   core/wsgi.py
        new file:   manage.py

### 3. Create django app 'blog' inside 'apps' folder

		E:\202009projects\django\ytb_developer.pe\blog-app-in-union (main)
		(venv39221) λ mkdir apps
		
		E:\202009projects\django\ytb_developer.pe\blog-app-in-union (main)
		(venv39221) λ cd apps\

		E:\202009projects\django\ytb_developer.pe\blog-app-in-union\apps (main)
		(venv39221) λ touch __init__.py

		E:\202009projects\django\ytb_developer.pe\blog-app-in-union\apps (main)
		(venv39221) λ django-admin startapp blog

		E:\202009projects\django\ytb_developer.pe\blog-app-in-union\apps (main)
		(venv39221) λ cd ..

		E:\202009projects\django\ytb_developer.pe\blog-app-in-union (main)
		(venv39221) λ python manage.py runserver
		Watching for file changes with StatReloader
		Performing system checks...

		System check identified no issues (0 silenced).

		You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
		Run 'python manage.py migrate' to apply them.

		December 25, 2020 - 08:54:52
		Django version 2.2.1, using settings 'core.settings'
		Starting development server at http://127.0.0.1:8000/

        modified:   README.md
        new file:   apps/__init__.py
        new file:   apps/blog/__init__.py
        new file:   apps/blog/admin.py
        new file:   apps/blog/apps.py
        new file:   apps/blog/migrations/__init__.py
        new file:   apps/blog/models.py
        new file:   apps/blog/tests.py
        new file:   apps/blog/views.py
        modified:   core/settings.py

### 4. Project settings, mingrations and superuser

        modified:   README.md
        modified:   core/settings.py

### 5. Model - Create Categoria and Autor models, register them and run migrations 

        modified:   README.md
        modified:   apps/blog/admin.py
        new file:   apps/blog/migrations/0001_initial.py
        modified:   apps/blog/models.py

### 6. Admin panel - modify display admin panel for categoria and autor

        modified:   README.md
        modified:   apps/blog/admin.py

### 7. django-import-export : Install and configure django-import-export for Categoria and Autor models

        modified:   README.md
        modified:   apps/blog/admin.py
        modified:   core/settings.py

### 8. Model - Create Post model, register it to admin and run migrations

        modified:   README.md
        modified:   apps/blog/admin.py
        new file:   apps/blog/migrations/0002_post.py
        modified:   apps/blog/models.py

### 9. Django CKEditor - Install and configuration

        >> pip install django-ckeditor
        >> impor to blog model
        >> use it in Post model
        >> register it to settings for full options of the CKEditor
        >> run migrations
        modified:   README.md
        new file:   apps/blog/migrations/0003_auto_20201225_1232.py
        modified:   apps/blog/models.py
        modified:   core/settings.py

### 10. Static files and template - Add static files and index template

        modified:   README.md
        new file:   apps/blog/urls.py
        modified:   apps/blog/views.py
        modified:   core/settings.py
        modified:   core/urls.py
        new file:   static/css/clean-blog.css
        new file:   static/css/clean-blog.min.css
        new file:   static/img/about-bg.jpg
        ...
        new file:   static/vendor/jquery/jquery.slim.js
        new file:   static/vendor/jquery/jquery.slim.min.js
        new file:   static/vendor/jquery/jquery.slim.min.map
        new file:   templates/about.html
        new file:   templates/contact.html
        new file:   templates/index.html
        new file:   templates/post.html

### 11. Template Inheritance with categories - Create templates and dynamic links

        modified:   README.md
        modified:   apps/blog/urls.py
        modified:   apps/blog/views.py
        new file:   static/img/general.jpg
        new file:   static/img/programming.jpg
        new file:   static/img/technology.jpg
        new file:   static/img/tutorial.jpg
        new file:   static/img/tutorial.png
        new file:   static/img/videogame.jpg
        new file:   templates/general.html
        modified:   templates/index.html
        new file:   templates/programming.html
        new file:   templates/technology.html
        new file:   templates/tutorial.html
        new file:   templates/videogame.html












































































































































































