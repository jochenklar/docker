.PHONY: default daemon up down logs clean logs env

default: env daemon

daemon:
	docker-compose up -d

up:
	docker-compose up

down:
	docker-compose down

build:
	docker-compose build

bash:
	docker-compose exec -it db bash

clean:
	docker-compose down -v

logs:
	docker-compose logs -f

env:
	touch .env
