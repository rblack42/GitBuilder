REPOS = _repos

.PHONY: lint
lint: 
	flake8 .

.PHONY: reqs
reqs: ## Install python requirements
	pip install -r requirements.txt

.PHONY: test
test:
	nosetests .

.PHONY: clean
clean:
	rm -rf $(REPOS)/* 
