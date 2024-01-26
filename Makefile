runserver:
	uvicorn main:app --reload
start:
	poetry shell 
startDb:
	docker-compose up -d 