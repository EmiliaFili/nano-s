
clean:
	-rm -rf build
	-rm -rf dist
	-rm -rf nano.egg-info
	-rm -rf htmlcov .coverage
	-find . -path ./.tox -prune -o -name '*.pyc' -exec rm -rf {} \;
	-find . -path ./.tox -prune -o -type d -empty -exec rmdir {} \;
