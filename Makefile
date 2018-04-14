all:
	docker-compose build

run:
	docker-compose up project

shell:
	docker-compose run --rm project /bin/bash

test:
	docker-compose run --rm project ./manage.py test

stop:
	docker-compose down