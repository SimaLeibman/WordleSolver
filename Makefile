.PHONY: help run run-input

VENV := .venv
PYTHON := $(VENV)/bin/python

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  help       Show this help (default)"
	@echo "  run        Run run_input.py using .venv"
	@echo "  run-input  Alias for run"

run run-input:
	$(PYTHON) run_input.py
