#!bin/sh
FLASK_APP=app1.py flask run --host=0.0.0.0 --port=4999 &
FLASK_APP=app2.py flask run --host=0.0.0.0 --port=4998 &