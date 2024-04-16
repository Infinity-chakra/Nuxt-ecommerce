#!/bin/sh

# Run linting
echo "Running linting..."
npm run lint

# Run tests
echo "Running tests..."
npm run test

# If any of the above commands fail, exit with a non-zero status code
if [ $? -ne 0 ]; then
    echo "Pre-commit checks failed. Please fix the issues before committing."
    exit 1
fi

# If everything passes, continue with the commit
exit 0