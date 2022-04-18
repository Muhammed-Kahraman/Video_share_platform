# Video_share_platform

1) Create a virtual environment
2) Install django
3) Create .env file same directory manage.py
4) And inside the file set up django_secret_key, aws_secret_key, access_key and bucket_name.
5) Install the packages written below.

Necessary steps for run the project
- pip install python-decouple

- pip install django_cleanup

- pip install django-storages

- pip install whitenoise      

- pip install django-crispy-forms

- pip install Boto3

- python manage.py migrate

And you are good to go.

Blog list View

List all blog posts with Title, Author Name, Date Posted, Video.

Search

List all blog posts with the search query that you enter.

Blog Detail View

To view the complete blog post when clicked  on the Title.

Login/Register

Users can Login/Register to the Blog App.

Comment

Users can comment to any blog post after login process.

Create Blog Post

Users can create blog posts from the front end and add for approval, by the admin.

Tech Stacks

- Language: Python 3.8
- Framework: Django 4.0.3
- AWS S3
