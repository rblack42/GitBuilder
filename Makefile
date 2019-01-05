REPOS = _repos

.PHONY: lint
lint: ## Run Python style checks using Flake8
	flake8 .

.PHONY: reqs
reqs: ## Install python requirements
	pip install -r requirements.txt

.PHONY: test
test: ## RUn unit tests on project
	nosetests .

.PHONY: html
html: ## generate html doc pages for GitHub
	cd rst && \
		sphinx-build -b html -d _build/doctrees . ../docs

.PHONY: clean
clean: ## Remove build artifacts 
	rm -rf $(REPOS)/* 
