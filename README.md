# Next_Up
Clone and download the repo
Open the downloaded folder in pycharm as open existing project
pycharm will detect requirements.txt and download all the dependencies
if you're not using pycharm, go to the project directory in the terminal and pip install all the dependencies(good luck with that)
cd bus_app in the terminal window in pycharm (the 1st one) and type the following:

- python manage.py makemigrations (if it doesnt work, delete all the pycache folders and retry)
- python manage.py migrate
- python manage.py runserver

If all goes will, within moments you'll get a link in the console, you can also manually type localhost:8000, you'll get a simple boring homepage with login and signup links
