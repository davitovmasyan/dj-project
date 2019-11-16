all:
	docker-compose build

run:
	docker-compose up project

shell:
	docker-compose run --rm project /bin/bash

test:
	docker-compose run --rm project pytest -x -vvv --pdb

report:
	docker-compose run --rm project pytest --cov=apps/ -x --pdb

report-html:
	docker-compose run --rm project pytest --cov-report html --cov=apps/ -x --pdb

sort:
	docker-compose run --rm project isort --recursive apps project

check-sort:
	docker-compose run --rm project isort --recursive --diff apps project

stop:
	docker-compose down