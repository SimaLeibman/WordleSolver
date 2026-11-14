.PHONY: help run run-input run-pattern install

VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  help       Show this help (default)"
	@echo "  "
	@echo "  install    ==> Run this first! Configure Python (.venv)"
	@echo "  "
	@echo "  run        Run run_input.py using .venv"
	@echo "  run-input  Alias for run"
	@echo "  run-pattern Run run_pattern.py using .venv"
	@echo "  run-sima Run the original main using .venv"

install:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	@if [ -f requirements.txt ]; then $(PIP) install -r requirements.txt; fi

run run-input:
	$(PYTHON) run_input.py

run-pattern:
	$(PYTHON) run_pattern.py

run-sima:
	$(PYTHON) main.py
