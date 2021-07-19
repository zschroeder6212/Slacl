.PHONY: start-dev build-prod bootstrap clean lint test
.DEFAULT_GOAL := test

test: lint
	@py.test test/ --cov=./main.py -s

lint:
	@flake8 .

clean:
	@find . -type f -name '*.pyc' -delete

start-dev:
	@yarn webpack --mode development --watch & ./venv/bin/python3 ./app/main.py

bootstrap:
	@pip install -r requirements.txt
	@pip install -r requirements-test.txt
	@python setup.py develop
	@yarn install

build-prod: bootstrap
	@yarn webpack --mode production

install: build-prod
	@mkdir -p /opt/slacl
	@cp -a ./app/* /opt/slacl
	@cp slacl.service /etc/systemd/system/slacl.service
	@systemctl enable slacl.service
	@systemctl start slacl.service

uninstall:
	systemctl stop slacl.service
	systemctl disable slacl.service
	@rm /etc/systemd/system/slacl.service
