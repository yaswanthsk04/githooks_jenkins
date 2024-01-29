#!/bin/bash

# Run unit tests
pytest

#coverage tests
coverage run -m pytest

# Run integration tests
pytest tests/test_gui_integration.py

# Exit with non-zero status if tests fail
if [ $? -ne 0 ]; then
    echo "Tests failed. Commit aborted."
    exit 1
fi
