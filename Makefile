app-run:
	poetry run uvicorn api.main:app --reload

docker-app-run:
	docker compose up --build

pre-commits:
	poetry run pre-commit run --all-files