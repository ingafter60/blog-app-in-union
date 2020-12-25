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