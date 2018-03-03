REPO = pypi
VENV_DIR = $(HOME)/.virtualenvs
VENV_NAME = ${VENV_DIR}/pickle-secure
PYTHON_BIN_DIR = ${VENV_NAME}/bin
PYTHON = ${PYTHON_BIN_DIR}/python
PIP = ${PYTHON_BIN_DIR}/pip

.PHONY: venv install version dist upload

venv:
	mkdir -p ${VENV_DIR}
	virtualenv ${VENV_NAME}

install:
	${PIP} install -e .

version:
	sed -i "/^__version__/c\__version__ = '${VER}'" setup.py
	git add setup.py
	git commit -m "Bump version to ${VER}"
	git tag -s ${VER} -m ${VER}
	git push --follow-tags

dist:
	-rm dist/*
	${PYTHON} setup.py sdist bdist_wheel

upload:dist
	twine upload --repository ${REPO} --sign dist/*
