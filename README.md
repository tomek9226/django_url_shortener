Simple URL Shortener Web App
===========================

Shorten long URLs into 6-character codes. Built with Django.

**Features**
* Shorten any URL to 6-char code
* Instant redirects to original URL
* Auto-generates unique codes
* Simple clean UI
* Admin panel to view all URLs

**Project Structure**
url_shortener/
├── venv/                    # Python virtual environment
├── manage.py                # Django commands
├── url_shortener/           # Django project folder
│   ├── init.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── urls/                    # Main Django app
├── migrations/
├── templates/
│   └── index.html
├── init.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py


**Setup**
1. **Clone/Download** this project

2. **Create virtual environment:**
   ```bash
   python -m venv venv

3. Activate
   Windows: venv\Scripts\activate
   macOS/Linux: source venv/bin/activate

4. Install Django:
pip install django

5. Run migrations:
python manage.py makemigrations
python manage.py migrate

6. Start server:
python manage.py runserver

7. Open browser: http://127.0.0.1:8000
