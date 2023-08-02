# this recipe is just for local use, do not use 'make test' for CI/CD as it 
# ignores the return value for the unit test program
.PHONY test:
test:
	-python -m coverage run -m pytest -v
	-python -m coverage report --show-missing

.PHONY dependencies:
dependencies:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt