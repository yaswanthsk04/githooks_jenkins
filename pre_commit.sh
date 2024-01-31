#!/bin/bash

# Run unit tests
pytest

#Run unit test & coverage tests
coverage run -m pytest tests/unit_test && coverage report

# Run integration & coverage tests
coverage run -m pytest tests/integration_test && coverage report

# Exit with non-zero status if tests fail
if [ $? -ne 0 ]; then
    echo "Tests failed. Commit aborted."
    exit 1
fi
