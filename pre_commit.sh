#!/bin/bash

# Exit the script if any command fails
set -e

# Run unit tests
pytest

# Run unit test & coverage tests
coverage run -m pytest tests/unit_test && coverage report

# Run integration & coverage tests
coverage run -m pytest tests/integration_test && coverage report

# If the script reaches this point, all tests have passed
echo "All tests passed successfully."
