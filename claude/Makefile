.PHONY: run build clean logs

run:
	docker compose run --rm claude

build:
	docker compose build

clean:
	docker compose down
	rm -fr claude workspace

logs:
	docker compose logs -f
