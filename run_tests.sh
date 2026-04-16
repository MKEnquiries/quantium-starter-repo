#!/bin/bash

# Activate the project's virtual environment
source venv/bin/activate

# Run the test suite
pytest test_app.py

# Capture pytest's exit code and exit with the same code
TEST_EXIT_CODE=$?

if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Tests failed."
    exit 1
fi
