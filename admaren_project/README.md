Setup Instructions


1. Clone the repository

git clone https://github.com/aswathypushkaran/machine_test
cd admaren_project


2. Create and activate a virtual environment (recommended)

Linux/macOS:

python3 -m venv env
source env/bin/activate

3. Install dependencies

pip install -r requirements.txt

5. Apply migrations

python manage.py makemigrate 
python manage.py migrate

6. Create a superuser (for admin access)

python manage.py createsuperuser

7. Run the development server

python manage.py runserver


API Usage

1. Obtain JWT tokens by hitting the login endpoint (/api/token/).

Use the access token in the Authorization header to access protected endpoints.

2. Refresh tokens via /api/token/refresh/.

3. Endpoints Added:

    Overview API: /api/notes/summary
    
    List notes: /api/notes/

    Create note: /api/notes/ (POST)

    Update note: /api/notes/<id>/ (PUT)
    
    Detail note: /api/notes/<id>/ (GET)

    Delete note: /api/notes/<id>/ (DELETE)

    List tags: /api/tags/

    Notes by tag: /api/tags/<tag_id>/notes/