test:
	python manage.py test

coverage:
	make test
	echo "Run coverage ... Done"

yamllint:
	echo "Run yamllint ... Done"

black:
	black .

build:
	python -m build

install:
	make build
	pip install dist/*.whl

uninstall:
	pip uninstall otus-open-lesson -y
	rm -rf dist
	rm -rf otus_open_lesson.egg-info

reinstall:
	make uninstall
	make install

pylint:
	echo "Run pylint ... Done"

lint:
	make yamllint
	make pylint
