.PHONY: test

test:
	python -m black --check *.py **/*.py
	python -m mypy --strict *.py **/*.py