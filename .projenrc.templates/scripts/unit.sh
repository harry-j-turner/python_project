#!/bin/bash

export ENVIRONMENT=LOCAL_TESTING
poetry run pytest  --cov -s
