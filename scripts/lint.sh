#!/bin/bash -xe

poetry run mypy --ignore-missing-imports cruft/
poetry run isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=100 --recursive --check --diff --recursive cruft/ tests/
poetry run black --check -l 100 cruft/ tests/
poetry run flake8 cruft/ tests/ --max-line 100 --ignore F403,F401,W503
poetry run safety check
poetry run bandit -r cruft/
