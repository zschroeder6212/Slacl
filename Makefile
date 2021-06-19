.PHONY: bootstrap clean lint test
.DEFAULT_GOAL := test

test: lint
	@py.test test/ --cov=./main.py -s

lint:
	@flake8 .

clean:
	@find . -type f -name '*.pyc' -delete

bootstrap:
	@pip install -r requirements.txt
	@pip install -r requirements-test.txt
	@python setup.py develop

install: bootstrap
	@mkdir -p /opt/slacl
	@cp -a ./app/* /opt/slacl
	@cp slacl.service /etc/systemd/system/slacl.service
	@systemctl enable slacl.service
	@systemctl start slacl.service

uninstall:
	systemctl stop slacl.service
	systemctl disable slacl.service
	@rm /etc/systemd/system/slacl.service
