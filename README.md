# Next_Up
- Clone and download the repo.
- Open the downloaded folder in pycharm as open existing project.
- pycharm will detect requirements.txt and download all the dependencies.
- if you're not using pycharm, go to the project directory in the terminal and pip install all the dependencies(good luck with that).
- cd bus_app in the terminal window in pycharm (the 1st one) and type the following:

- python manage.py makemigrations (if it doesnt work, delete all the pycache folders and retry)
- python manage.py migrate
- python manage.py createsuperuser (create a username, valid emailid and a password)
- python manage.py runserver

If all goes will, within moments you'll get a link in the console, go to it, or you can also manually type localhost:8000, you'll get a simple boring homepage with login and signup links. Then if you go to localhost:8000/admin you can login with the username and password that you created and get a django-admin page. 

### For Google Single Signon
- get credentials fill up stuff as required, set authorised redirect uri as http://localhost:8000/accounts/google/login/callback/ and click download client id.
- Go to localhost:8000/admin -> sites -> change domain name to 127.0.0.1 -> go back -> go to soacial applications in socialaccounts -> add Gmail, client id, secret key, add 127.0.0.1 and save.
- Go to home.html, add {% loadsocialaccount %}, add link <a href={% provider_login_url 'google' %}>Sign in with Google</a>
- In settings.py set SITE_ID=2
