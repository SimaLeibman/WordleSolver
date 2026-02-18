.PHONY: help run run-input run-pattern

VENV := .venv
PYTHON := $(VENV)/bin/python

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  help       Show this help (default)"
	@echo "  run        Run run_input.py using .venv"
	@echo "  run-input  Alias for run"
	@echo "  run-pattern Run run_pattern.py using .venv"
	@echo "  run-sima Run the original main using .venv"

run run-input:
	$(PYTHON) run_input.py

run-pattern:
	$(PYTHON) run_pattern.py

run-sima:
	$(PYTHON) main.py
