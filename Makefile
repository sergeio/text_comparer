PYTHON = python

.PHONY: test tdd clean dist upload

test:
	nosetests tests/*.py

tdd:
	nosyd -1

clean:
	-$(PYTHON) setup.py clean
	-find . -type f -name '*.pyc' -o -name '*.tar.gz' -delete
	-rm -f nosetests.xml
	-rm -f pip-log.txt
	-rm -f .nose-stopwatch-times
	-rm -rf build dist *.egg-info

dist: clean
	$(PYTHON) setup.py sdist

upload:
	$(PYTHON) setup.py sdist upload
