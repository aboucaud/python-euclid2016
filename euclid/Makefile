PHONY: clean test coverage

clean:
	find . -type f -name "*.pyc" -delete
	find . -type f -name "__pycache__" -delete

test:
	py.test -v

coverage:
	py.test --cov euclid/
