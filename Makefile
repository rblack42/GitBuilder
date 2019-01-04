.PHONY: reqs
reqs: ## Install python requirements
	pip install -r requirements.txt

.PHONY: test
test:
	nosetests .
	flake8 .