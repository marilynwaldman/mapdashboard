install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest -vv test_application.py

lint:
	#pylint --disable=R,C application.py

deploy:
	echo "Deploying app"
	eb deploy dash-map-env

all:   install  deploy 