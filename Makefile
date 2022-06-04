.PHONY = test

test:
	python -m black --check *.py 
	python -m mypy --strict *.py 