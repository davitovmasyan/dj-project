all:
	docker-compose build
	docker-compose run --rm packages cp -r  /usr/local/lib/python3.6/site-packages /host

run:
	docker-compose up project

shell:
	docker-compose run --rm project /bin/bash

test:
	docker-compose run --rm project pytest --create-db -x --pdb

report:
	docker-compose run --rm project pytest --cov=apps/ --create-db -x --pdb

report-html:
	docker-compose run --rm project pytest --cov-report html --cov=apps/ --create-db -x --pdb

sort:
	docker-compose run --rm project isort --recursive apps project

check-sort:
	docker-compose run --rm project isort --recursive --diff apps project

stop:
	docker-compose down