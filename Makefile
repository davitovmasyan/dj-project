all:
	docker-compose build

run:
	docker-compose up project

shell:
	docker-compose run --rm project /bin/bash

test:
	docker-compose run --rm project pytest -x -vvv --pdb --create-db

report:
	docker-compose run --rm project pytest --cov=apps/ -x --pdb --create-db

report-html:
	docker-compose run --rm project pytest --cov-report html --cov=apps/ -x --pdb --create-db

sort:
	docker-compose run --rm project isort apps project

check-sort:
	docker-compose run --rm project isort --diff apps project

stop:
	docker-compose down