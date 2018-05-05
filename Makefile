all:
	docker-compose build

run:
	docker-compose up project

shell:
	docker-compose run --rm project /bin/bash

test:
	docker-compose run --rm project pytest

stop:
	docker-compose down