.PHONY build:
build:
	@python -m build

# this recipe is just for local use, do not use 'make test' for CI/CD as it 
# ignores the return value for the unit test program
.PHONY test:
test:
	@python -m coverage run -m pytest -v
	@python -m coverage report --show-missing
	@python -m coverage erase

.PHONY deps:
deps:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt
	python -m pip install -r dev-requirements.txt