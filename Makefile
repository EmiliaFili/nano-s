
clean:
	-rm -rf build
	-rm -rf dist
	-rm -rf nano.egg-info
	-rm -rf htmlcov .coverage
	-find . -name "*.py?" -delete
	-find . -name __pycache__ -delete
	-find . -path ./.tox -prune -o -name '*.py?' -exec rm -rf {} \;
	-find . -path ./.tox -prune -o -type d -empty -exec rmdir {} \;
