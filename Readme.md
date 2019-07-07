Quick list of shortcuts:

When making modifications to models:
	heroku run python manage.py makemigrations
	heroku run python manage.py migrate

When Updating static:
	heroku run python manage.py collectstatic

To update code:
	git add --all
	git commit -m ""
	git push heroku master

When in urgent debugging cases:
	1) Check Urls,views and models
	2) check for the 'i' esp. when copy/paste
	3) Check html file
	4) just re-deploy

For AWS S3 assistance, 
	Contact Sean

For AWS S3,
	1) Upload files there and remember exact name
	2) Please dont stupid and delete things
	3) just ask before touching the bucket

Lastly, 
	Enjoy this program