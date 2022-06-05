.PHONY: test static_analysis unit_tests

test: static_analysis unit_tests

static_analysis:
	python -m black --check *.py **/*.py
	python -m mypy --strict *.py **/*.py

unit_tests:
	python -m nose2