.PHONY: up clean

up:
	docker-compose up

register:
	docker-compose run runner register  # Executor should be `docker`

clean:
	docker-compose rm && rm -r volumes
