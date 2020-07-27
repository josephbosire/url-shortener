.PHONY: $(MAKECMDGOALS)

# Builds docker image
setup:
	cd docker && docker-compose build

# Launches docker container with application listening on port 8005
server:
	cd docker && docker-compose down
	cd docker && docker-compose up -d shortener
	cd docker && docker-compose exec shortener python manage.py migrate

# `make test` will be used after `make setup` in order to run
# your test suite.
test:
	nox

