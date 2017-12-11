build:
	docker build -t Supermarket .
run:
	docker run -e SKUS="${SKUS}" -it Supermarket
