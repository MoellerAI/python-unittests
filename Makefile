test:
	cd app && \
    poetry run pytest --cov=src tests/ --cov-report=xml:cobertura.xml --cov-report term-missing