VENV   := .venv
PYTHON := $(VENV)/bin/python
PIP    := $(VENV)/bin/pip

.DEFAULT_GOAL := help
.PHONY: help venv install run run-input run-pattern run-sima test clean

help: ## Show this help
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n\nTargets:\n"} \
		/^[a-zA-Z0-9_-]+:.*##/ { printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

# Sentinel file: only re-runs when requirements.txt changes or venv is missing
$(VENV)/.installed: requirements.txt
	@test -d $(VENV) || python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@touch $@

venv: $(VENV)/.installed ## Create/update the virtualenv

install: venv ## Alias for venv

run: run-input ## Alias for run-input

run-input: venv ## Run run_input.py
	$(PYTHON) run_input.py

run-pattern: venv ## Run run_pattern.py
	$(PYTHON) run_pattern.py

run-sima: venv ## Run main.py
	$(PYTHON) main.py

test: venv ## Run the test suite
	$(PYTHON) -m pytest

clean: ## Remove the virtualenv
	rm -rf $(VENV)
