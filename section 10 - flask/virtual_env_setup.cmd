# If running on Python 3, just run
#python3 -m venv flask

python -m virtualenv flask

#start a new cmd, then run
#cmd
flask/Scripts/activate.bat

pip install flask
pip install gunicorn # this is http server

pip freeze > requirements.txt

# create Procfile (no extension):
#web: gunicorn flask1:app

#create runtime.txt, otherwise herocu will use default one which is python 2.7 (https://devcenter.heroku.com/articles/python-runtimes#supported-python-runtimes)

#flask/Scripts/deactivate.bat
